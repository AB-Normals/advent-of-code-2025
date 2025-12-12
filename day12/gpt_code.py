
# solve_presents.py
from typing import List, Tuple, Dict, Set

def parse_shapes_and_regions(text: str):
    lines = [l.rstrip() for l in text.splitlines()]
    shapes: Dict[int, List[str]] = {}
    regions: List[Tuple[int,int,List[int]]] = []
    i = 0
    # Parse shapes
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        if ':' in line and line.split(':')[0].isdigit():
            idx = int(line.split(':')[0])
            i += 1
            grid = []
            while i < len(lines) and lines[i] and not (('x' in lines[i]) and (':' in lines[i])):
                grid.append(lines[i])
                i += 1
            shapes[idx] = grid
        else:
            break
    # Parse regions
    while i < len(lines):
        line = lines[i]
        if not line:
            i += 1
            continue
        left, right = line.split(':')
        w_str, h_str = left.split('x')
        w, h = int(w_str), int(h_str)
        counts = [int(x) for x in right.strip().split()] if right.strip() else []
        regions.append((w, h, counts))
        i += 1
    max_idx = max(shapes.keys())
    ordered_shapes = [shapes[i] for i in range(max_idx+1)]
    return ordered_shapes, regions

# Geometry utilities
def grid_to_points(grid: List[str]) -> Set[Tuple[int,int]]:
    return {(x,y) for y,row in enumerate(grid) for x,ch in enumerate(row) if ch == '#'}

def normalize_points(pts: Set[Tuple[int,int]]):
    minx = min(x for x, y in pts)
    miny = min(y for x, y in pts)
    return tuple(sorted(((x - minx, y - miny) for x, y in pts)))

def transform_points(pts: Set[Tuple[int,int]], op: str):
    mirror = op.startswith('F')
    r = int(op[-1])
    def rot(p):
        x, y = p
        if r == 0: return (x, y)
        if r == 1: return (-y, x)
        if r == 2: return (-x, -y)
        if r == 3: return (y, -x)
    pts2 = pts
    if mirror:
        pts2 = {(-x, y) for x, y in pts2}
    return {rot(p) for p in pts2}

def unique_orientations(pts: Set[Tuple[int,int]]):
    variants = set()
    for op in ['rot0','rot1','rot2','rot3','Frot0','Frot1','Frot2','Frot3']:
        variants.add(normalize_points(transform_points(pts, op)))
    return sorted(list(variants))

def shape_area(norm_pts): return len(norm_pts)
def shape_bounds(norm_pts):
    maxx = max(x for x, y in norm_pts)
    maxy = max(y for x, y in norm_pts)
    return (maxx+1, maxy+1)

def build_placements(W: int, H: int, shapes_grids: List[List[str]]):
    shapes_pts = [grid_to_points(g) for g in shapes_grids]
    shapes_orients = [unique_orientations(pts) for pts in shapes_pts]
    placements_by_shape: List[List[Tuple[Set[int], Tuple[int,int], Tuple[Tuple[int,int], ...]]]] = []
    cell_index = { (x,y): y*W + x for y in range(H) for x in range(W) }
    for orients in shapes_orients:
        shape_list = []
        for norm in orients:
            bw, bh = shape_bounds(norm)
            for oy in range(H - bh + 1):
                for ox in range(W - bw + 1):
                    cells = {cell_index[(ox+dx, oy+dy)] for (dx,dy) in norm}
                    shape_list.append((cells, (ox, oy), norm))
        placements_by_shape.append(shape_list)
    areas = [shape_area(orients[0]) for orients in shapes_orients]
    return placements_by_shape, areas

def can_fit_region(W: int, H: int, counts: List[int], shapes_grids: List[List[str]], need_solution: bool=False):
    placements_by_shape, areas = build_placements(W, H, shapes_grids)
    total_area = sum(c*a for c,a in zip(counts, areas))
    if total_area > W*H:
        return False, None

    pieces: List[int] = []
    for si, cnt in enumerate(counts):
        pieces.extend([si]*cnt)
    if not pieces:
        return True, ['.'*W for _ in range(H)] if need_solution else None

    # Heuristic: try the most constrained pieces first
    pieces.sort(key=lambda si: len(placements_by_shape[si]))

    occupied: Set[int] = set()
    selection: List[Tuple[int, Tuple[Set[int], Tuple[int,int], Tuple[Tuple[int,int], ...]]]] = []

    def backtrack(idx: int) -> bool:
        if idx == len(pieces): return True
        si = pieces[idx]
        # Placements filtered by current occupancy
        candidates = [p for p in placements_by_shape[si] if not (p[0] & occupied)]
        # Optional: sort by centrality to find solutions faster
        for cells, tl, norm in candidates:
            selection.append((si, (cells, tl, norm)))
            occupied.update(cells)
            if backtrack(idx+1):
                return True
            for c in cells: occupied.remove(c)
            selection.pop()
        return False

    feasible = backtrack(0)
    if not feasible:
        return False, None

    if not need_solution:
        return True, None

    # Render a grid with letters A,B,C,... per shape index
    grid = [['.' for _ in range(W)] for _ in range(H)]
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for si, (cells, tl, norm) in selection:
        letter = letters[si]
        ox, oy = tl
        for dx, dy in norm:
            grid[oy+dy][ox+dx] = letter
    return True, [''.join(row) for row in grid]

# ---- Example usage on your sample ----
if __name__ == "__main__":
    sample = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""
    shapes, regions = parse_shapes_and_regions(sample)
    fits = 0
    for (W, H, counts) in regions:
        ok, grid = can_fit_region(W, H, counts, shapes, need_solution=True)
        print(f"{W}x{H} {counts} -> {'FIT' if ok else 'NO FIT'}")
        if ok and grid:
            print("\n".join(grid))
            print()
        if ok: fits += 1
    print("Total regions that fit:", fits)

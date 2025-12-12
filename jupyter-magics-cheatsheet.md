
# Jupyter/IPython Magic Commands Cheat Sheet

This cheat sheet covers **cell magics** (`%%...`) and **line magics** (`%...`) and **shell escapes** (`!...`) with concise tables and practical examples.

---

## 🧩 Cell Magics (`%%`)

> Cell magics apply to the **entire cell**.

| Magic | Description |
|---|---|
| `%%capture` | Capture cell output (stdout & stderr). Options: `--no-stderr`, `--no-stdout`. |
| `%%time` | Time a single execution of the cell. |
| `%%timeit` | Benchmark the cell by running multiple times and reporting statistics. |
| `%%writefile <path>` | Write the cell content to a file (overwrites by default). |
| `%%bash` | Run the cell as a Bash script. |
| `%%html` | Render the cell content as HTML. |
| `%%latex` | Render LaTeX math and text. |
| `%%markdown` | Render Markdown content in the cell. |
| `%%javascript` | Execute JavaScript in the notebook frontend. |
| `%%svg` | Render inline SVG markup. |
| `%%script <lang>` | Run the cell with a given script engine (e.g., `bash`, `ruby`, `perl`). |
| `%%python` | (IPython) Explicitly run the cell with Python (useful inside multi-language notebooks). |
| `%%file <path>` | Alias of `%%writefile` in some environments (if available). |

### Examples: Cell Magics

#### `%%capture`
```python
%%capture --no-stderr
print("This stdout will be hidden")
import sys; print("This stderr will be shown", file=sys.stderr)
```

Capture into a variable and show later:
```python
%%capture cap
print("Stored output")
# Later in another cell
cap.show()
```

#### `%%time`
```python
%%time
# One run timing
sum(i*i for i in range(10_000_000))
```

#### `%%timeit`
```python
%%timeit
# Multiple runs with statistics
sum(i*i for i in range(1_000_000))
```

#### `%%writefile`
```python
%%writefile example.py
import sys
print("Hello from file")
```

#### `%%bash`
```bash
%%bash
echo "Hello from Bash"
uname -a
```

#### `%%html`
```html
%%html
<div style="padding:8px;border:1px solid #ccc">Rendered <b>HTML</b> block</div>
```

#### `%%latex`
```latex
%%latex
$$\int_0^1 x^2\,dx = \frac{1}{3}$$
```

#### `%%markdown`
```markdown
%%markdown
# Title inside the cell
- Bullet 1
- Bullet 2
```

#### `%%javascript`
```javascript
%%javascript
alert("Hello from JavaScript")
```

#### `%%svg`
```svg
%%svg
<svg width="120" height="60" xmlns="http://www.w3.org/2000/svg">
  <rect width="120" height="60" fill="lightblue"/>
  <text x="10" y="35" font-size="16">SVG text</text>
</svg>
```

#### `%%script`
```python
%%script bash
echo "Using the generic script magic with Bash"
```

---

## 🧠 Line Magics (`%`)

> Line magics apply to a **single line**.

| Magic | Description |
|---|---|
| `%lsmagic` | List all available line and cell magics. |
| `%time` | Time a single statement. |
| `%timeit` | Benchmark a single statement multiple times. |
| `%pip install <pkg>` | Install Python packages in the current kernel environment. |
| `%conda install <pkg>` | Install packages via conda (if available in the kernel). |
| `%matplotlib inline` | Render Matplotlib plots inline (classic backend). |
| `%matplotlib widget` | Use interactive Matplotlib widgets in Jupyter. |
| `%pwd` | Print current working directory. |
| `%cd <path>` | Change current working directory. |
| `%history` | Show command history. Options: `-n`, `-o`, `-p`. |
| `%load <url_or_path>` | Load code into a cell from a file or URL. |
| `%run <script.py>` | Run a Python script in the current kernel. |
| `%edit <script.py>` | Open an editor to modify or create a script, then run it. |
| `%reset` | Reset namespace (options to confirm or force). |
| `%who` / `%whos` | List variables in the interactive namespace. |
| `%env` | Get/set environment variables. |
| `%xmode` | Exception reporting mode: `Plain`, `Context`, `Verbose`. |
| `%precision <n>` | Set floating-point display precision. |
| `%pinfo <obj>` | Show help (same as `obj?`). |
| `%pinfo2 <obj>` | Detailed help (same as `obj??`). |
| `%alias` | Define an alias for a system command. |
| `%config` | Configure IPython extensions and objects (e.g., `InlineBackend.figure_format`). |
| `%load_ext <module>` | Load an IPython extension. |
| `%reload_ext <module>` | Reload a previously loaded extension. |
| `%unload_ext <module>` | Unload an IPython extension. |
| `%autoreload` | Automatically reload modules when their source changes (with `autoreload` extension). |
| `%debug` | Enter the interactive debugger after an exception. |
| `%tb` | Print the traceback from the last exception. Options: `-s` (short), `-l` (long). |
| `%save <path> <n-m>` | Save input history (lines `n` to `m`) to a file. |
| `%recall <n>` | Recall input line `n` into the current cell. |
| `%store` | Store/retrieve variables across sessions. |
| `%bookmark` | Manage directory bookmarks (`%bookmark -l` to list). |
| `%rehashx` | Recompute command aliases from `$PATH`. |
| `%system` | Run a system command (similar to `!cmd`). |

### Examples: Line Magics

#### `%lsmagic`
```python
%lsmagic
```

#### `%time`
```python
%time sum(range(10_000_000))
```

#### `%timeit`
```python
%timeit [x*x for x in range(10000)]
```

#### `%pip`
```python
%pip install -q tqdm
```

#### `%conda`
```python
%conda install -y numpy
```

#### `%matplotlib`
```python
%matplotlib inline
```

#### `%pwd` and `%cd`
```python
%pwd
%cd /tmp
```

#### `%history`
```python
%history -n -o 1-10  # show input numbers and outputs for lines 1-10
```

#### `%load`
```python
%load https://raw.githubusercontent.com/psf/requests/main/requests/__init__.py
```

#### `%run`
```python
%run example.py
```

#### `%edit`
```python
%edit example.py
```

#### `%reset`
```python
%reset -f  # force without confirmation
```

#### `%who` / `%whos`
```python
%who
%whos
```

#### `%env`
```python
%env MY_VAR=hello
%env MY_VAR
```

#### `%xmode`
```python
%xmode Verbose
```

#### `%precision`
```python
%precision 4
import math
math.pi  # will display with 4 decimals
```

#### `%pinfo` / `%pinfo2`
```python
%pinfo str
%pinfo2 str
```

#### `%alias`
```python
%alias ll ls -alF
ll
```

#### `%config`
```python
%config InlineBackend.figure_format = 'retina'
```

#### `%load_ext` / `%reload_ext` / `%unload_ext`
```python
%load_ext autoreload
%reload_ext autoreload
%unload_ext autoreload
```

#### `%autoreload`
```python
# Enable the autoreload extension and set the mode
%load_ext autoreload
%autoreload 2  # reload all modules (except those excluded)

# Now, modifying a module's source will reflect without restarting the kernel
import mymodule  # edits to mymodule.py will be picked up automatically
```

#### `%debug`
```python
# After an exception occurs, run:
%debug  # enter post-mortem debugger (pdb)
```

#### `%tb`
```python
# Show the traceback for the last exception
%tb -l  # long form
```

#### `%save`
```python
# Save lines 1 to 20 of input history to a file
%save session_commands.py 1-20
```

#### `%recall`
```python
# Recall line 12 into the current cell for editing/execution
%recall 12
```

#### `%store`
```python
x = 42
%store x  # persist value across sessions
# Later or in another session:
%store -r x
print(x)
```

#### `%bookmark`
```python
%bookmark mytmp /tmp
%bookmark -l  # list bookmarks
%cd -b mytmp  # cd to bookmark
```

#### `%rehashx`
```python
%rehashx  # refresh command aliases from PATH
```

#### `%system`
```python
%system echo "Hello via %system"
```

---

## 🖥️ Shell Escapes with `!` (grep & pipes)

You can run **shell commands** directly from a notebook with `!`. This is useful to quickly inspect files, filter output with `grep`, and chain commands using **pipes** (`|`).

> ℹ️ On Windows, replace `grep` with `findstr` and some options may differ.

### Basic listing and filtering
```bash
!ls -la | grep ".py$"          # list all files and keep only Python files
!ls -1 data | grep -i "csv"      # case-insensitive match for CSV files in data/
```

### Grep with context and line numbers
```bash
!grep -n "ERROR" logs/app.log            # show matching lines with numbers
!grep -nC2 "timeout" logs/app.log        # 2 lines of context around matches
!grep -R "TODO" src/                      # recursive search in src/
```

### Combining multiple pipes
```bash
# Count unique import statements across .py files
!grep -Rh "^import \|^from" src/ \
  | sed 's/#.*$//' \
  | awk 'NF' \
  | sort \
  | uniq -c \
  | sort -nr | head
```

### Searching inside notebooks (JSON) for a string
```bash
!grep -R "tqdm" -n --include "*.ipynb" . | head
```

### Using `!` and capturing output in Python
```python
# Capture the output of a shell pipeline into a Python list
py_files = !ls -1 | grep -i ".py$"
len(py_files), py_files[:5]
```

### Windows equivalents (PowerShell)
```powershell
# List and filter using findstr (regex-like)
!dir /b | findstr /i ".py$"

# Search recursively for a string
!findstr /s /n /i "ERROR" logs\*.log
```

**Tips**
- Prefer `%pip` over `!pip` to ensure installation in the kernel's environment.
- You can redirect streams: `> /dev/null` hides stdout; `2>/dev/null` hides stderr.
- Use `!python -m pip ...` to guarantee the interpreter matches the kernel.

---

## Notes
- Availability of some magics depends on your IPython/Jupyter environment and installed extensions.
- In VS Code notebooks, output rendering may differ from classic Jupyter Notebook.
- Use `%lsmagic` anytime to see exactly what is supported in your current kernel.


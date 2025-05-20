# 🐍 Python 3 CLI Cheat Sheet
```
    Yahyaoui Med Aziz  | 2025   
```
### 📌 Basic Usage

| Command                     | Description                                   |
| --------------------------- | --------------------------------------------- |
| `python3` or `python`       | Start interactive shell (REPL)                |
| `python3 file.py`           | Run a Python script                           |
| `python3 -m module`         | Run a module as a script (e.g. `venv`, `pip`) |
| `python3 -V` or `--version` | Show Python version                           |
| `python3 -c "code"`         | Run inline Python code                        |

---

### ⚙️ Virtual Environments

#### Built-in venv

| Command                                   | Description                  |
| ----------------------------------------- | ---------------------------- |
| `python3 -m venv myenv`                   | Create a virtual environment |
| `source myenv/bin/activate` (Linux/macOS) | Activate environment         |
| `myenv\Scripts\activate.bat` (Windows)    | Activate (Windows CMD)       |
| `deactivate`                              | Exit virtual environment     |

#### Older alternative: `virtualenv`

| Command                  | Description             |
| ------------------------ | ----------------------- |
| `pip install virtualenv` | Install virtualenv tool |
| `virtualenv myenv`       | Create virtualenv       |

---

### 📦 Package Management — `pip`

| Command                           | Description                              |
| --------------------------------- | ---------------------------------------- |
| `pip install package`             | Install package                          |
| `pip uninstall package`           | Uninstall package                        |
| `pip list`                        | List installed packages                  |
| `pip freeze`                      | Output installed packages (requirements) |
| `pip freeze > requirements.txt`   | Save dependencies                        |
| `pip install -r requirements.txt` | Install from file                        |
| `pip show package`                | Show package info                        |

---

### 🚀 Modern Environment Management

#### ✅ Poetry (dependency & environment manager)

| Command                             | Description                     |
| ----------------------------------- | ------------------------------- |
| `pip install poetry`                | Install Poetry                  |
| `poetry init`                       | Start new project interactively |
| `poetry new myproj`                 | Create new project structure    |
| `poetry shell`                      | Spawn a new shell within venv   |
| `poetry install`                    | Install dependencies            |
| `poetry add package`                | Add a new package               |
| `poetry remove package`             | Remove a package                |
| `poetry update`                     | Update all dependencies         |
| `poetry run python file.py`         | Run file in the environment     |
| `poetry export -f requirements.txt` | Export requirements file        |

#### ⚡ `uv` (ultra-fast dependency manager, drop-in replacement for pip + venv)
> 📝 `uv` can be used just like `pip` and `venv`, but faster. Poetry + uv is a powerful combo!

| Command                               | Description                    |
|---------------------------------------| ------------------------------ |
| `pip install uv`                      | Install uv                     |
| `uv venv`                             | Create virtual environment     |
| `uv pip install package`              | Install packages super fast    |
| `uv pip list`                         | List packages                  |
| `uv pip freeze`                       | Freeze dependencies            |
| `uv pip install -r requirements.txt`  | Install from file (ultra-fast) |

##### 📜 `uv` Full Command List (from `uv --help`):

| Command   | Description                                                             |
|-----------|-------------------------------------------------------------------------|
| `run`     | Run a command or script                                                 |
| `init`    | Create a new project                                                    |
| `add`     | Add dependencies to the project                                         |
| `remove`  | Remove dependencies from the project                                    |
| `sync`    | Update the project's environment                                        |
| `lock`    | Update the project's lockfile                                           |
| `export`  | Export the project's lockfile to an alternate format                    |
| `tree`    | Display the project's dependency tree                                   |
| `tool`    | Run and install commands provided by Python packages `uv run packname`  |
|           | or for tool you can just utilize `uvx`                                  |
| `python`  | Manage Python versions and installations                                |
| `pip`     | Manage Python packages with a pip-compatible interface                  |
| `venv`    | Create a virtual environment                                            |
| `build`   | Build Python packages into source distributions and wheels              |
| `publish` | Upload distributions to an index                                        |
| `cache`   | Manage `uv`'s cache                                                     |
| `self`    | Manage the `uv` executable                                              |
| `version` | Read or update the project's version                                    |
| `help`    | Display documentation for a command                                     |

---

---

### 🛠️ Debugging & Performance

| Command                            | Description                    |
| ---------------------------------- | ------------------------------ |
| `python3 -m pdb script.py`         | Run script with debugger       |
| `python3 -m timeit "code"`         | Time small bits of Python code |
| `python3 -X tracemalloc script.py` | Memory allocation tracking     |

---

### 🧪 Testing

| Command                            | Description         |
| ---------------------------------- | ------------------- |
| `python3 -m unittest`              | Run all unittests   |
| `python3 -m unittest test_file.py` | Run tests in a file |

---

### 🔍 Help & Info

| Command                | Description                |
| ---------------------- | -------------------------- |
| `python3 -h`           | Help overview              |
| `python3 -m module -h` | Help for a specific module |



### 🧹 Ruff — Fast Python Linter & Formatter

| Command                         | Description                                   |
| ------------------------------- | --------------------------------------------- |
| `pip install ruff`              | Install Ruff                                  |
| `ruff check .`                  | Lint the current directory                    |
| `ruff check file.py`            | Lint a specific file                          |
| `ruff check --fix .`            | Lint and auto-fix issues                      |
| `ruff format .`                 | Format all files like `black`                 |
| `ruff format file.py`           | Format a specific file                        |
| `ruff --help`                   | View help and command options                 |
| `ruff --output-format json`     | Output lint results in JSON format            |
| `ruff check --select F401`      | Lint only specific rules (e.g. unused import) |
| `ruff check --ignore E501`      | Ignore specific rules (e.g. line length)      |
| `ruff check --config ruff.toml` | Use custom config file                        |

---

### ⚡ Ruff with `uv` (super fast virtual env + install)

| Command                          | Description                         |
| -------------------------------- | ----------------------------------- |
| `uv venv`                        | Create a virtual environment        |
| `uv pip install ruff`            | Install Ruff using `uv`             |
| `uv pip run ruff check .`        | Lint current directory (via uv run) |
| `uv pip run ruff format file.py` | Format a file with Ruff             |
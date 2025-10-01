# Py File Organizer

Automatically sort your files into folders based on their extension and keep your directories tidy.

## Overview
- Detects every file extension and moves the file to the matching folder defined in `py_file_organizer/extensions.py`.
- Ships with a console-menu based interface so you can run it interactively.
- Provides basic error handling for missing or already organized directories.

## Prerequisites
- Python 3.8 or newer.
- `pip` available on your PATH.
- A virtual environment is optional but recommended.

## Environment setup
```bash
# clone the repository
git clone https://github.com/silviooosilva/Py-File-Organizer.git
cd Py-File-Organizer

# (optional) create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate

# application dependencies
pip install -r requirements.txt

# development and testing dependencies
pip install -r requirements_dev.txt
```

## How to run the organizer
```bash
python3 -m py_file_organizer.main
# or pass the target directory directly
python3 -m py_file_organizer.main /path/to/directory
```
Without arguments the program opens an interactive menu: choose `Start App`, paste the absolute path of the directory you want to organize, and confirm. When you supply the directory as a CLI argument the organization runs immediately, which is handy for automation. Folders are created according to the mapping in `py_file_organizer/extensions.py`.

## Testing and quality checks
### Unit tests
```bash
python3 -m pytest tests/ -v
```
Or use the Makefile shortcut with coverage:
```bash
make tests
```

### BDD scenarios
```bash
python3 -m pytest bdd/ -v
```
Or run:
```bash
make bdd
```

### Lint
```bash
flake8 .
```
(The `make lint` command runs the tests with coverage first and then executes flake8.)

## Project layout
```
py_file_organizer/
├── main.py            # Console-menu interface and CLI entrypoint
├── functions.py       # File organization logic
├── extensions.py      # Extension-to-folder mapping
└── __init__.py
```
Unit tests live in `tests/`, BDD scenarios in `bdd/`, and demo screenshots in `demo/`.

## Contributing
Feel free to open issues or pull requests. Before submitting changes, run the test suite (`make tests`) and the linter (`flake8 .`) to ensure everything still works.

## License
Released under the MIT License. See `LICENSE` for details.

## Author
Project created by Silvio Silva.

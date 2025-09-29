# Release Notes

## v2.0 - Py File Organizer

### Highlights
- Rewrote the project README with updated setup, execution, and testing instructions to match the current workflow.
- Documented optional virtual environment usage and separated runtime dependencies from development-only tooling.
- Clarified how to run the interactive console menu (`python3 -m py_file_organizer.main`) and outlined the extension mapping in `py_file_organizer/extensions.py`.
- Added explicit guidance for running unit tests, BDD scenarios, and linting through both raw commands and Makefile shortcuts.

### Fixed / Improved
- Streamlined onboarding steps for contributors by grouping all prerequisites and commands in one place.
- Reduced ambiguity around coverage reporting flags used in `make tests` by ensuring the necessary plugins are installed via `requirements_dev.txt`.

### Testing
- `make tests`
- `make bdd`
- `flake8 .`

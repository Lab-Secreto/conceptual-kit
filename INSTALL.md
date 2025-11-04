# Installation Guide

## Quick Install

### Using uv (Recommended)

```bash
# Install from GitHub
uv tool install conceptual-kit --from git+https://github.com/Lab-Secreto/conceptual-kit.git

# Or install locally for development
uv tool install --editable .
```

### Using pip

```bash
# Install from GitHub
pip install git+https://github.com/Lab-Secreto/conceptual-kit.git

# Or install locally for development
pip install -e .
```

---

## Local Development Installation

If you want to develop or test the CLI locally:

### 1. Install Dependencies

```bash
# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"
```

### 2. Test the CLI

```bash
# Check version
conceptual version

# Check system requirements
conceptual check

# Initialize a test project
conceptual init test-project --ai claude

# Or in current directory
mkdir temp-test
cd temp-test
conceptual init . --ai claude --force
```

### 3. Run Tests (when added)

```bash
pytest
```

---

## Verify Installation

After installation, verify everything works:

```bash
# Check the CLI is installed
which conceptual

# Check version
conceptual --version

# Check system requirements
conceptual check

# See help
conceptual --help
```

**Expected output:**
```
Usage: conceptual [OPTIONS] COMMAND [ARGS]...

  Conceptual Kit - Create comprehensive conceptual models for your
  applications.

  Based on Johnson & Henderson's Conceptual Models Framework.

Options:
  --version   Show the version and exit.
  --help      Show this message and exit.

Commands:
  check    Check system requirements and configuration.
  init     Initialize a new conceptual modeling project.
  version  Show version information.
```

---

## Testing the Full Workflow

```bash
# 1. Create a test directory
mkdir ~/conceptual-test
cd ~/conceptual-test

# 2. Initialize a project
conceptual init my-app --ai claude

# 3. Check what was created
cd my-app
ls -la

# Expected structure:
# .
# ├── .git/
# ├── .github/
# │   └── copilot-instructions.md
# ├── .gitignore
# ├── README.md
# ├── conceptual-modeling.md
# ├── docs/
# ├── examples/
# │   ├── e-commerce/
# │   ├── google-calendar/
# │   └── todo-app/
# └── templates/
#     ├── base-model.md
#     └── components/

# 4. Read the philosophy guide
cat conceptual-modeling.md

# 5. Check examples
ls examples/

# 6. Use with Claude Code (if installed)
claude "concept init TestApp"
```

---

## Troubleshooting

### Command not found

If `conceptual` command is not found after installation:

```bash
# Check if it's in your PATH
which conceptual

# If using uv, ensure uv bin directory is in PATH
echo $PATH | grep uv

# Add to PATH if needed (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"
```

### Import errors

If you get import errors:

```bash
# Reinstall with dependencies
pip install -e ".[dev]"

# Or check installed packages
pip list | grep conceptual
```

### Templates not found

If templates are not being copied:

```bash
# Check templates exist in source
ls templates/

# Reinstall
pip uninstall conceptual-kit
pip install -e .
```

---

## Uninstalling

```bash
# Using uv
uv tool uninstall conceptual-kit

# Using pip
pip uninstall conceptual-kit
```

---

## For Contributors

### Setting up development environment

```bash
# 1. Clone the repository
git clone git@github-secreto:Lab-Secreto/conceptual-kit.git
cd conceptual-kit

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate

# 3. Install in editable mode with dev dependencies
pip install -e ".[dev]"

# 4. Install pre-commit hooks (when added)
pre-commit install

# 5. Run tests
pytest

# 6. Format code
black conceptual_kit/
ruff check conceptual_kit/

# 7. Type check
mypy conceptual_kit/
```

### Building for distribution

```bash
# 1. Install build tools
pip install build twine

# 2. Build the package
python -m build

# 3. Check the distribution
twine check dist/*

# 4. Upload to PyPI (requires account)
twine upload dist/*
```

---

## System Requirements

- **Python:** 3.8 or higher
- **Git:** (optional) for version control
- **Pandoc:** (optional) for PDF generation

Check requirements:
```bash
conceptual check
```

---

## Optional Dependencies

### For PDF Generation

```bash
# Install pandoc
# macOS
brew install pandoc

# Ubuntu/Debian
sudo apt-get install pandoc

# Windows
choco install pandoc
```

### For Development

```bash
# Install with dev dependencies
pip install -e ".[dev]"

# This includes:
# - pytest (testing)
# - black (code formatting)
# - mypy (type checking)
# - ruff (linting)
```

---

## Getting Help

- **Documentation:** See `README.md` and `conceptual-modeling.md`
- **Examples:** Check `examples/` directory
- **Issues:** Report at https://github.com/Lab-Secreto/conceptual-kit/issues
- **Validation:** See `VALIDATION_REPORT.md` for quality assurance

---

Happy modeling! 🎨🧠

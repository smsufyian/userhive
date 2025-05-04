# UserHive

A FastAPI-based application for user management.

## Setup

### Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd userhive
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Set up pre-commit hooks:
   ```bash
   # Make the setup script executable
   chmod +x setup_hooks.sh

   # Run the setup script
   ./setup_hooks.sh
   ```

   Alternatively, you can manually install the pre-commit hooks:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

### Running the project locally:

```bash
# Run the FastAPI application
python -m src.userhive.app
```

Or use the verify script to test that the API is working:

```bash
python verify_api.py
```

## Development

### Pre-commit Hooks

This project uses pre-commit hooks to ensure code quality. The hooks will run automatically when you commit changes, and will:

1. Format code using Black
2. Sort imports using isort
3. Check for linting issues using flake8
4. Run tests using pytest

If any of these checks fail, the commit will be aborted. You'll need to fix the issues and try committing again.

### Running Hooks Manually

You can run the pre-commit hooks manually without committing:

```bash
pre-commit run --all-files
```

Or run a specific hook:

```bash
pre-commit run black --all-files
pre-commit run isort --all-files
pre-commit run flake8 --all-files
pre-commit run pytest --all-files
```

### Running Tests

```bash
pytest
```

## Troubleshooting

### Pre-commit Hooks Not Working

If the pre-commit hooks are not working, make sure:

1. Pre-commit is installed: `pip install pre-commit`
2. Hooks are installed in the git repository: `pre-commit install`
3. The `.pre-commit-config.yaml` file is properly configured

You can also try reinstalling the hooks:

```bash
pre-commit uninstall
pre-commit install
```

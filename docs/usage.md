# MyPackage Usage Guide

## Installation

```bash
# Clone the repository
git clone <repository-url>
cd mypackage

# Install dependencies
uv sync

# Install pre-commit hooks (optional)
uv run pre-commit install
```

## Running the API Server

### Development Mode
```bash
# Using uv
uv run uvicorn mypackage.api:app --reload

# Or using the Makefile
make dev
```

### Production Mode
```bash
# Using uv
uv run uvicorn mypackage.api:app --host 0.0.0.0 --port 8000

# Or using the Makefile
make serve
```

The API will be available at `http://localhost:8000`

## Using the CLI

```bash
# Show help
mypackage --help

# Run wisdom extraction on a repository
mypackage run /path/to/repository

# Check system status
mypackage status
```

## Development Workflow

### Running Tests
```bash
# Run all tests
uv run pytest

# Run with coverage
uv run pytest --cov=mypackage

# Run specific test file
uv run pytest tests/test_api.py
```

### Code Quality
```bash
# Format code
make format

# Lint code
make lint

# Run all quality checks
make format lint test
```

### Pre-commit Hooks
If you installed pre-commit hooks, they will automatically run on each commit:
- Code formatting with Ruff
- Linting with Ruff

## Configuration

Create a `.env` file in the project root:

```env
# API Configuration
HOST=0.0.0.0
PORT=8000
```

## Architecture

MyPackage consists of several key components:

- **API Layer** (`mypackage/api.py`): FastAPI web server
- **CLI Layer** (`mypackage/cli.py`): Command-line interface
- **Core Logic** (`mypackage/core/`):
  - `custom_thing.py`: Your package custom logic
- **Data Models** (`mypackage/models/`): Pydantic models for API contracts

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Run `make format lint test`
6. Submit a pull request

## Troubleshooting

### Import Errors
Make sure the package is installed:
```bash
uv sync
```

### Port Already in Use
```bash
# Find process using port 8000
lsof -ti:8000 | xargs kill -9

# Or use a different port
uv run uvicorn mypackage.api:app --port 8001
```

### Test Failures
```bash
# Run tests with verbose output
uv run pytest -v

# Run specific failing test
uv run pytest tests/test_api.py::test_custom_thing_endpoint -s
```

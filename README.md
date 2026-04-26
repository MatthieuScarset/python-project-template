# 🛡️ MyPackage: Python project template

**MyPackage** do custom things with ease. Make it yours.

### 🛠️ Technical Stack

This project uses a modern, minimal Python stack focused on fast APIs,
clear data validation, and simple CLIs. Key components:

- **Language:** Python 3.14+
- **Web framework:** FastAPI (ASGI, high-performance HTTP API)
- **Server:** Uvicorn (ASGI server)
- **Data models & settings:** Pydantic v2 + pydantic-settings
- **CLI:** Typer (simple, intuitive CLI builders)
- **HTTP client:** httpx
- **Testing:** pytest, pytest-asyncio, pytest-cov
- **Code quality:** mypy, pre-commit (formatters / linters)
- **Packaging:** pyproject.toml (PEP 621)

## 🚀 Quick Start

Install and run the API server:

```bash
cd mypackage/
uv sync
make dev  # Runs with auto-reload
```

Do a custom thing:

```bash
source .venv/bin/activate && \
curl -X POST "http://localhost:8000/custom-thing" \
  -H "Content-Type: application/json" \
  -d '{"data": "Hellomoto\nHolamota"}'
```

Built with ❤️ by [Matthieu Scarset](https://matthieuscarset.com).

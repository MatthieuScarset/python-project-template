"""Test configuration and fixtures."""

import pytest
from fastapi.testclient import TestClient

from mypackage.api import app


@pytest.fixture
def client():
    """FastAPI test client."""
    return TestClient(app)


@pytest.fixture
def lorem_ipsum():
    """Sample data for testing."""
    return """This is a sample data string for testing custom-thing endpoints.
    It can be a git diff or any text input that the API expects to process.
    The content can be adjusted based on the actual use case and expected
    input format of the API.
"""

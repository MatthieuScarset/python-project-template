"""Tests for MyPackage CLI."""

import pytest
from typer.testing import CliRunner

from mypackage.cli import app


@pytest.fixture
def runner():
    """CLI test runner."""
    return CliRunner()


def test_cli_help(runner):
    """Test CLI help command."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "MyPackage" in result.output


def test_cli_run_command_help(runner):
    """Test run command help."""
    result = runner.invoke(app, ["run", "--help"])
    assert result.exit_code == 0
    assert "mypackage" in result.output.lower()


def test_cli_status_command(runner):
    """Test status command."""
    result = runner.invoke(app, ["status"])
    assert result.exit_code == 0
    assert "MyPackage" in result.output


def test_cli_run_command_missing_repo(runner):
    """Test run command with missing repo argument."""
    result = runner.invoke(app, ["run"])
    assert result.exit_code == 2  # Missing required argument
    assert "Missing argument" in result.output or "required" in result.output.lower()


def test_cli_run_command_with_repo(runner, tmp_path):
    """Test run command with repo argument."""
    # Create a fake repo directory
    repo_dir = tmp_path / "fake_repo"
    repo_dir.mkdir()

    result = runner.invoke(app, ["run", str(repo_dir)])
    assert result.exit_code == 0
    # Should show some output about processing
    assert len(result.output.strip()) > 0

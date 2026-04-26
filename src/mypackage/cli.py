#!/usr/bin/env python3
"""
MyPackage CLI - Do custom things

A command-line interface for MyPackage, an intelligent system that do custom things.
"""

import typer

app = typer.Typer(
    name="mypackage",
    help="MyPackage: Python project template",
    add_completion=False,
)


@app.command()
def run(
    myarg: str = typer.Argument(..., help="Something to get into account"),
    verbose: bool = typer.Option(
        False,
        "--verbose",
        "-v",
        help="Enable verbose logging.",
    ),
) -> None:
    """
    Run the MyPackage service.
    """
    typer.echo("🚀 Starting MyPackage")

    if verbose:
        typer.echo("📝 Verbose mode enabled")
        typer.echo(f"📁 Doing something with argument: {myarg}")

    # TODO: Implement the actual guardian logic
    # - Do something
    # - Do something else
    # - ...
    # - Display results

    typer.echo("⚠️ MyPackage logic not yet implemented - this is a placeholder CLI")


@app.command()
def status() -> None:
    """
    Check the status of MyPackage.
    """
    typer.echo("📊 Checking MyPackage status...")

    # TODO: Implement status checks

    typer.echo("✅ CLI is ready (backend integration pending)")


if __name__ == "__main__":
    app()

"""custom-thing functionality for MyPackage."""

from typing import Any


class CustomThing:
    """Do custom things."""

    def __init__(self):
        self.stats = {}

    def custom_thing(self, data: str) -> dict[str, Any]:
        """
        Do a custom thing.

        Args:
            data: Raw data content

        Returns:
            dictionary with results
        """
        lines = data.split("\n")

        analysis = {
            "total_lines": len(lines),
        }

        return analysis

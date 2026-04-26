"""Tests for MyPackage core modules."""

import pytest

from mypackage.core.custom_thing import CustomThing


class TestCustomThing:
    """Test CustomThing functionality."""

    @pytest.fixture
    def custom_thing(self):
        return CustomThing()

    def test_custom_thing_basic(self, custom_thing, lorem_ipsum):
        """Test basic custom-thing."""
        result = custom_thing.custom_thing(lorem_ipsum)

        assert "total_lines" in result
        assert result["total_lines"] > 0

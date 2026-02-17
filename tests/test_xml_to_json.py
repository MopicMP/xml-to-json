"""Tests for xml-to-json."""

import pytest
from xml_to_json import json


class TestJson:
    """Test suite for json."""

    def test_basic(self):
        """Test basic usage."""
        result = json("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            json("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = json(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities

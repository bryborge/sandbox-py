import pytest
from greetings import greeting


class TestGreetingsModule:
    """Test Greeting Module structure."""

    def test_greeting(self):
        """Test that the greeting function returns the expected message."""
        result = greeting()
        assert result == "Hello World"


    def test_greeting_is_string(self):
        """Test that the greeting function returns a string."""
        result = greeting()
        assert isinstance(result, str)


    def test_greeting_not_empty(self):
        """Test that the greeting function doesn't return an empty string."""
        result = greeting()
        assert len(result) > 0

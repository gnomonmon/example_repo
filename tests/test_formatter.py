import pytest
from mypackage.formatter import Formatter


@pytest.fixture
def formatter():
    return Formatter()


def test_formatter_to_uppercase(formatter):
    assert formatter.to_uppercase("hello") == "HELLO"
    assert formatter.to_uppercase("World") == "WORLD"


def test_formatter_to_lowercase(formatter):
    assert formatter.to_lowercase("HELLO") == "hello"
    assert formatter.to_lowercase("World") == "world"


def test_formatter_to_title_case(formatter):
    assert formatter.to_title_case("hello world") == "Hello World"
    assert formatter.to_title_case("foo bar baz") == "Foo Bar Baz"


def test_formatter_truncate_short_string(formatter):
    assert formatter.truncate("hi", 10) == "hi"


def test_formatter_truncate_long_string(formatter):
    result = formatter.truncate("hello world", 5)
    assert result == "hello..."
    assert len(result) == 8

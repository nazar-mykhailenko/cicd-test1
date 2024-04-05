import pytest
from src.main import filter_lines


@pytest.mark.parametrize("lines, keyword, expected", [
    (["hello world", "goodbye world", "hello goodbye"], "hello", ["hello world", "hello goodbye"]),
    (["hello world", "goodbye world", "hello goodbye"], "goodbye", ["goodbye world", "hello goodbye"]),
    (["hello world", "goodbye world", "hello goodbye"], "world", ["hello world", "goodbye world"])
])
def test_filter_lines(lines, keyword, expected):
    assert filter_lines(lines, keyword) == expected

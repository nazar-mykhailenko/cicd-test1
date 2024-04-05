import pytest


@pytest.fixture
def prepare_file(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("hello world\ngoodbye world\nhello goodbye")
    return input_file


@pytest.fixture
def prepare_empty_file(tmp_path):
    input_file = tmp_path / "input.txt"
    input_file.write_text("")
    return input_file

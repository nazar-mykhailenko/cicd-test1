import pytest
import src.main as main


@pytest.mark.parametrize("text_to_write", [
    "hello world\ngoodbye world\nhello goodbye",
    "goodbye world\nhello goodbye",
    "hello world\ngoodbye world"
])
def test_write_file(text_to_write):
    output_file = "output.txt"
    main.write_to_file(output_file, text_to_write)
    with open(output_file, "r") as file:
        lines = file.readlines()
    assert lines == text_to_write.splitlines(True)


def teardown_function(function):
    import os
    os.remove("output.txt")

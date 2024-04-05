import src.main as main


def test_read_file(prepare_file):
    lines = main.read_file(prepare_file)
    assert lines == ["hello world\n", "goodbye world\n", "hello goodbye"]


def test_read_empty_file(prepare_empty_file):
    lines = main.read_file(prepare_empty_file)
    assert lines == []

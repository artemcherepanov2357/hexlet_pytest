from hexlet_pytest.example import reverse


def test_reverse():
    assert reverse("Hexlet") == "telxeH"


def test_reverse_for_empty_string():
    assert reverse("") == ""


from pathlib import Path


def get_test_data_path(filename):
    return Path(__file__).parent / "test_data" / filename


def read_file(filename):
    return get_test_data_path(filename).read_text()


def test_reverse_long_text():
    input_text = read_file("input.txt")
    expected = read_file("expected.txt")

    assert reverse(input_text) == expected

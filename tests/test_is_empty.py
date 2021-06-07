from testing import is_empty


def test_empty_list():
    assert is_empty([1, 2, 3]) is False


def test_empty_dict():
    assert is_empty({"item": 1}) is False


def test_empty_tuple():
    assert is_empty(()) is True


def test_integer_is_false():
    assert is_empty(1) is False

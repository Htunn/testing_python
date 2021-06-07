def test_long_strings():
    string = ("This has a very long string")
    expected = ("This is a very long, string")
    assert string == expected

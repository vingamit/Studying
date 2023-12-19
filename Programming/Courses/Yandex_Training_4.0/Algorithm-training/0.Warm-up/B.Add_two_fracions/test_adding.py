from adding import add_fraction


def test_add():
    assert add_fraction([1, 2, 1, 2]) == (1, 1)
    assert add_fraction([1, 3, 1, 3]) == (2, 3)
    assert add_fraction([16, 50, 17, 25]) == (1, 1)
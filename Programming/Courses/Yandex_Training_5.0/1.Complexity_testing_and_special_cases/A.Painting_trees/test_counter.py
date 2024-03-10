from paint_count import count_painted


def test_cnt():
    assert count_painted((0, 7), (12, 5)) == 25
    assert count_painted((0, 1), (1, 1)) == 4
from anagram import anagram_func


def test_ana() -> None:
    assert anagram_func('dusty', 'study') == 'YES'
    assert anagram_func('rat', 'bat') == "NO"
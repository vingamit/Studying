from collections import Counter


def anagram_func(one: str, two: str) -> str:
    fdi, sdi = Counter(one), Counter(two)
    if fdi == sdi:
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":
    first = input()
    second = input()
    print(anagram_func(first, second))
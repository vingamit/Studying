from typing import Tuple


def count_painted(va: Tuple[int, int],
                  ma: Tuple[int, int]) -> int:
    res = 0
    p, v, q, m = *va, *ma
    l1, r1, l2, r2 = p - v, p + v, q - m, q + m
    mas = sorted([(l1, r1), (l2, r2)])
    x1, x2, y1, y2 = *mas[0], *mas[1]
    if x2 < y1:
        res = x2 - x1 + y2 - y1 + 2
    elif y2 <= x2:
        res = x2 - x1 + 1
    else:
        res = y2 - x1 + 1
    return res


def main():
    v = tuple(map(int, input().split()))
    m = tuple(map(int, input().split()))
    
    res = count_painted(v, m)
    print(res)


if __name__ == "__main__":
    main()

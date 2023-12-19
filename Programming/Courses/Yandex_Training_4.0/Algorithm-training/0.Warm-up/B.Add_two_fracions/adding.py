from math import gcd
from typing import Tuple
from typing import List


def add_fraction(mas: List[int]) -> Tuple[int, int]:
    a, b, c, d = mas
    numerator = a * d + c * b
    denominator = b * d
    to_denomi = gcd(numerator, denominator)

    numerator //= to_denomi
    denominator //= to_denomi

    return numerator, denominator



if __name__ == "__main__":
    val = list(map(int, input().split()))
    print(*add_fraction(val))
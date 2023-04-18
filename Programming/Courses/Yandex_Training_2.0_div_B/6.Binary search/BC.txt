a, b, c, d = map(float, input().split())
if a < 0:
    a *= -1
    b *= -1
    c *= -1
    d *= -1
le = -10 ** 7
r = -le
de = 1e-7
while le < r:
    mi = (le + r) / 2
    if abs(le - r) < de:
        print(mi)
        break
    elif a * mi * mi * mi + b * mi * mi + c * mi + d > 0:
        r = mi
    else:
        le = mi

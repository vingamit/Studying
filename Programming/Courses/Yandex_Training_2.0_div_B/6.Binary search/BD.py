a, k, b, m, x = map(int, input().split())
le = 0
r = x * max(a, b)
while r - le > 1:
    mi = (le + r) // 2
    if (mi - mi // k) * a + (mi - mi // m) * b >= x:
        r = mi
    else:
        le = mi
print(int(r))

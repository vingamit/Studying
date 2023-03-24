n, k, m = map(int, input().split())
res = 0
if k >= m:
    while n >= k:
        do = res
        res += (n // k) * (k // m)
        n-= (res - do) * m
print(res)
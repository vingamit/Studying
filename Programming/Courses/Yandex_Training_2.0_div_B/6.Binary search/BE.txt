n, k = map(int, input().split())
mas = list(map(int, input().split()))
mas.sort()
le = 0
r = mas[-1] - mas[0]
while le < r:
    ll = (r + le) // 2
    ans = 0
    mar = mas[0] - 1
    for x in mas:
        if x > mar:
            ans += 1
            mar = x + ll
    if ans <= k:
        r = ll
    else:
        le = ll + 1
print(le)

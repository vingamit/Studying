ri = set()
ans = 0
with open('input.txt', 'r', encoding='UTF-8') as fil:
    n = int(fil.readline().rstrip())
    for i in range(n):
        a, b = map(int, fil.readline().rstrip().split())
        if a + b == n - 1:
            fi = (a * b) >= 0
            if (a, b) not in ri and fi:
                ans += 1
                ri.add((a, b))
print(ans)

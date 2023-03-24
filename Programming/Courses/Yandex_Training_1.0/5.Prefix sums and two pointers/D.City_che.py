with open('input.txt', 'r') as file:
    n, r = map(int, file.readline().rstrip().split())
    mas = list(map(int, file.readline().rstrip().split()))
le = 0
ri = 1
ans = 0
while le < n:
    while ri != n and mas[ri] - mas[le] <= r:
        ri += 1
    ans += n - ri
    le += 1
print(ans)

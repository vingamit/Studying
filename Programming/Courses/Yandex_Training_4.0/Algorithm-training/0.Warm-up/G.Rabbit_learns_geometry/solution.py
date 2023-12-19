n, m = map(int, input().split())
field = [[] for _ in range(n)]
for i in range(n):
    field[i] = list(map(int, input().split()))


dp = [[0 for _ in range(m)] for _ in range(n)]
dp[0] = field[0]
for i in range(n):
    dp[i][0] = field[i][0]


for i in range(1, n):
    for j in range(1, m):
        if field[i - 1][j - 1] == 1  and field[i - 1][j] == 1 and \
           field[i - 1][j] == 1 and field[i][j] == 1:
            el = min(dp[i - 1][j - 1], dp[i][j - 1], dp[i - 1][j])
            dp[i][j] = el + 1
        else:
            dp[i][j] = field[i][j]


print(max(max(row) for row in dp))
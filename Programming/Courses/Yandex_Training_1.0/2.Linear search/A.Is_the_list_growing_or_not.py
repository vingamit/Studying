spi = list(map(int, input().split()))
d = 0
for i in range(len(spi) - 1):
    if spi[i] >= spi[i + 1]:
        d = 1
if d == 0:
    print('YES')
else:
    print('NO')
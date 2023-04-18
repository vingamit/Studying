n, m = map(int, input().split())
stu = list(map(int, input().split()))
cla = list(map(int, input().split()))
cla = [(cla[i], i + 1) for i in range(m)]
stu = [(stu[i], i + 1) for i in range(n)]
di = {i + 1: 0 for i in range(n)}
i = 0
j = 0
amo = 0
cla.sort()
stu.sort()
while i < n and j < m:
    if cla[j][0] > stu[i][0]:
        di[stu[i][1]] = cla[j][1]
        j += 1
        i += 1
        amo += 1
    else:
        j += 1
print(amo)
for i in range(1, n + 1):
    print(di[i], end=' ')

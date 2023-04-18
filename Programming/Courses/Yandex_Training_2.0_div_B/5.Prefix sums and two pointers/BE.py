s = int(input())
a = list(map(int, input().split()))
a = a[1:]
b = list(map(int, input().split()))
b = b[1:]
c = list(map(int, input().split()))
c = c[1:]
di = dict()
for i in range(len(c)):
    if c[i] not in di:
        di[c[i]] = [i]
    else:
        di[c[i]].append(i)
d = 0
i = 0
j = 0
flag = True
while i < len(a) and flag:
    while j < len(b) and flag:
        if s - a[i] - b[j] in di:
            print(i, j, di[s - a[i] - b[j]][0])
            flag = False
            d = 1
        j += 1
    i += 1
    j = 0
if d == 0:
    print(-1)


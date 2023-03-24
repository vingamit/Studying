mas = list(map(int, input().split()))
mi = [float('inf'), float('inf'), float('inf')]
ma = [float('-inf'), float('-inf'), float('-inf')]
if len(mas) > 6:
    for i in mas:
        if i > ma[2]:
            ma[0] = ma[1]
            ma[1] = ma[2]
            ma[2] = i
        elif i > ma[1]:
            ma[0] = ma[1]
            ma[1] = i
        elif i > ma[0]:
            ma[0] = i
        if i < mi[0]:
            mi[2] = mi[1]
            mi[1] = mi[0]
            mi[0] = i
        elif i < mi[1]:
            mi[2] = mi[1]
            mi[1] = i
        elif i < mi[2]:
            mi[2] = i
    res = mi + ma
else:
    res = mas
res = [i for i in res if i != float('inf')]
res = [i for i in res if i != float('-inf')]
mi = float('-inf')
re = None
for i in range(len(res) - 2):
    for j in range(i+1, len(res) - 1):
        for k in range(i+2, len(res)):
            if res[i] * res[j] * res[k] > mi:
                mi = res[i] * res[j] * res[k]
                re = (res[i], res[j], res[k])
print(re[0], re[1], re[2])
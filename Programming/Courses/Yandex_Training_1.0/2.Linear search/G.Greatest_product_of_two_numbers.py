mas = list(map(int, input().split()))
lm, rm = float('inf'), float('inf')
lp, rp = float('-inf'), float('-inf')
for i in mas:
    if i > rp:
        lp = rp
        rp = i
    elif i > lp:
        lp = i
    if i < lm:
        rm = lm
        lm = i
    elif i < rm:
        rm = i
if lm * rm == float('inf'):
    print(lp, rp)
elif lp * rm == float('inf'):
    print(lm, rm)
elif lp * rp > lm * rm:
    print(lp, rp)
else:
    print(lm, rm)
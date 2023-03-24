ann = set()
bor = set()
with open('input.txt', 'r', encoding='UTF-8') as fil:
    n, m = map(int, fil.readline().rstrip().split())
    for i in range(n):
        nu = int(fil.readline().rstrip())
        ann.add(nu)
    for i in range(m):
        nu = int(fil.readline().rstrip())
        bor.add(nu)
inter = ann & bor
wan = ann - bor
wbo = bor - ann
print(len(inter))
if len(inter) == 0:
    print()
else:
    inter = list(inter)
    inter.sort()
    print(*inter)
print(len(wan))
if len(wan) == 0:
    print()
else:
    wan = list(wan)
    wan.sort()
    print(*wan)
print(len(wbo))
if len(wbo) == 0:
    print()
else:
    wbo = list(wbo)
    wbo.sort()
    print(*wbo)
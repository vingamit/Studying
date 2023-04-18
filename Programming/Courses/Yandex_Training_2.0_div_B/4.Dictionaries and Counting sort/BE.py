win = []
m = int(input())
for i in range(m):
    win.append(set(input()))
n = int(input())
di = {}
for i in range(n):
    cau = input()
    crn = cau
    cau = set(cau)
    d = 0
    for wi in win:
        if len(wi) == len(wi & cau):
            d += 1
    if d not in di:
        di[d] = [crn]
    else:
        di[d].append(crn)
print(*di[max(di)], sep='\n')
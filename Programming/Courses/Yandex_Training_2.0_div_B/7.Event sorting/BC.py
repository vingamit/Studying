with open('input.txt', 'r') as file:
    flag = True
    m = int(file.readline().rstrip())
    segm = []
    while flag:
        le, ri = map(int, file.readline().rstrip().split())
        if le == 0 and ri == 0:
            flag = False
        elif le < m and 0 < ri:
            segm.append((le, ri))
segm.sort()
edge = 0
nexd = 0
best = (0, 0)
ans = []
for seg in segm:
    if seg[0] > edge:
        ans.append(best)
        edge = nexd
        if edge >= m:
            break
    if seg[0] <= edge and seg[1] > nexd:
        nexd = seg[1]
        best = seg
if edge < m:
    edge = nexd
    ans.append(best)
if edge < m:
    print('No solution')
else:
    print(len(ans))
    for seg in ans:
        print(*seg)

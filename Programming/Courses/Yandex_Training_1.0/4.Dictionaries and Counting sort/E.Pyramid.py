n = int(input())
di = {}
for i in range(n):
    w, h = map(int, input().split())
    if w not in di:
        di[w] = h
    else:
        di[w] = max(h, di[w])
ans = sum(di[key] for key in di)
print(ans)
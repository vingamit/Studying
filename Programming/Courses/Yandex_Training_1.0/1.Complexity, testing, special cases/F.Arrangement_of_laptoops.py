f1, f2, s1, s2 = map(int, input().split())
res = []
res.append((f1 + s1, max(f2, s2)))
res.append((f1 + s2, max(f2, s1)))
res.append((f2 + s1, max(f1, s2)))
res.append((f2 + s2, max(f1, s1)))
res.sort(key=lambda x: x[0] * x[1])
print(res[0][0], res[0][1])
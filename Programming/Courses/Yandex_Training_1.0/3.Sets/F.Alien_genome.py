fi = input()
se = input()
sec = set()
for i in range(len(se) - 1):
    du = se[i:i + 2]
    sec.add(du)
res = 0
for i in range(len(fi) - 1):
    du = fi[i:i + 2]
    if du in sec:
        res += 1
print(res)

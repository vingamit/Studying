a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
fi = [a, b, c]
fi.sort()
se = [d, e]
se.sort()
j = 0
for i in range(len(fi)):
    if j == 2:
        pass
    else:
        if fi[i] <= se[j]:
            j += 1
if j != 2:
    print('NO')
else:
    print('YES')
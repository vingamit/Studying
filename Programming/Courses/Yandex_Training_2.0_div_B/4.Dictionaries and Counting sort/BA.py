n = int(input())
d = {}
mas = []
for i in range(n):
    fi,se = map(int,input().split())
    if fi not in d:
        d[fi] = se
        mas.append(fi)
    else:
        d[fi] += se
mas.sort()
for i in range(len(mas)):
    print(mas[i],d[mas[i]])
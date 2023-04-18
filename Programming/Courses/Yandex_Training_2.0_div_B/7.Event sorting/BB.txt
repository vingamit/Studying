n = int(input())
mas = []
for i in range(n):
    le, ri = map(int, input().split())
    mas.append((le, 1))
    mas.append((le + ri, -1))
mas.sort()
ol = 0
ma = ol
for i in range(len(mas)):
    if mas[i][1] == -1:
        ol -= 1
    else:
        ol += 1
    ma = max(ol, ma)
print(ma)

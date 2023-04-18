n = int(input())
mas = []
for i in range(n):
    le, ri = map(int, input().split())
    if le != ri:
        mas.append((le, -1))
        mas.append((ri, 1))
mas.sort()
ol = 0
total = 0
for i in range(len(mas)):
    if ol > 0:
        total += mas[i][0] - mas[i - 1][0]
    if mas[i][1] == -1:
        ol += 1
    else:
        ol -= 1
print(total)

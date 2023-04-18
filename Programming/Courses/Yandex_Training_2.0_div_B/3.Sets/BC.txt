lst = list(map(int,input().split()))
cont = set()
mas = []
for i in range(len(lst)):
    if lst[i] not in cont:
        cont.add(lst[i])
        mas.append(lst[i])
se_mas = [0]*len(mas)
for i in range(len(lst)):
    for j in range(len(se_mas)):
        if lst[i] == mas[j]:
            se_mas[j] += 1
for i in range(len(se_mas)):
    if se_mas[i] == 1:
        print(mas[i], end=' ')
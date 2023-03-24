alo = set()
with open('input.txt', 'r', encoding='UTF-8') as file:
    n = int(file.readline().rstrip())
    mas = [[] for i in range(n)]
    for i in range(n):
        m = int(file.readline().rstrip())
        for j in range(m):
            lan = file.readline().rstrip()
            mas[i].append(lan)
            alo.add(lan)
alk = alo.copy()
for i in range(n):
    alk.intersection_update(mas[i])
print(len(alk))
print(*alk, sep='\n')
print(len(alo))
print(*alo, sep='\n')
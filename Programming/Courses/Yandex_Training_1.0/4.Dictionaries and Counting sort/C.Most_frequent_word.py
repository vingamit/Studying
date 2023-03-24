di = {}
with open('input.txt', 'r', encoding='UTF-8') as fin:
    for line in fin:
        line = line.rstrip().split()
        for bunch in line:
            if bunch not in di:
                di[bunch] = 0
            else:
                di[bunch] += 1
mas = []
for key in di:
    mas.append((di[key], key))
mas.sort(key=lambda x: x[0], reverse=True)
ma = mas[0][0]
mas = [(key, val) for val, key in mas if val==ma]
mas.sort()
print(mas[0][0])
with open('input.txt', 'r') as f:
    line = f.read().splitlines()
d = {}
for i in range(len(line)):
    fe, se = line[i].split()
    line[i] = [fe,se]
    if line[i][0] not in d:
        d[line[i][0]] = int(line[i][1])
    else:
        d[line[i][0]] += int(line[i][1])
d = dict(sorted(d.items()))
for key in d:
    print(key,d[key])
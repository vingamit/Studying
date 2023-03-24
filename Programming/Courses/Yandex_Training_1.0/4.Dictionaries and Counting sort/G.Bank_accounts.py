di = {}
with open('input.txt', 'r', encoding='UTF-8') as fin:
    for line in fin:
        line = line.rstrip().split()
        if line[0] == 'DEPOSIT':
            if line[1] not in di:
                di[line[1]] = int(line[-1])
            else:
                di[line[1]] += int(line[-1])
        elif line[0] == 'WITHDRAW':
            if line[1] not in di:
                di[line[1]] = -int(line[-1])
            else:
                di[line[1]] -= int(line[-1])
        elif line[0] == 'BALANCE':
            if line[1] not in di:
                print('ERROR')
            else:
                print(di[line[1]])
        elif line[0] == 'TRANSFER':
            if line[1] not in di:
                di[line[1]] = -int(line[-1])
            else:
                di[line[1]] -= int(line[-1])
            if line[2] not in di:
                di[line[2]] = int(line[-1])
            else:
                di[line[2]] += int(line[-1])
        elif line[0] == 'INCOME':
            inc = int(line[-1])
            for key in di:
                if di[key] > 0:
                    di[key] += int(di[key] * inc / 100)
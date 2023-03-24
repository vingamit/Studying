di = {}
with open('input.txt', 'r', encoding='UTF-8') as fin:
    for line in fin:
        line = line.rstrip().split()
        for bunch in line:
            if bunch not in di:
                di[bunch] = 0
            else:
                di[bunch] += 1
            print(di[bunch], end=' ')
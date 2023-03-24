di = {}
with open('input.txt', 'r', encoding='UTF-8') as fin:
    for line in fin:
        line = line.rstrip().split()
        if line[0] not in di:
            di[line[0]] = {}
        if line[1] not in di[line[0]]:
            di[line[0]][line[1]] = int(line[2])
        else:
            di[line[0]][line[1]] += int(line[2])
cust = sorted(di)
for cus in cust:
    print(cus+':')
    lis = sorted(di[cus])
    for prod in lis:
        print(prod, di[cus][prod])
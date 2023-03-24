with open('input.txt', 'r') as file:
    n = int(file.readline().rstrip())
    mas = [0] * n
    fre = [0] * (n + 1)
    sre = [0] * (n + 1)
    for i in range(n):
        x, y = map(int, file.readline().rstrip().split())
        mas[i] = y
    pre = mas[0]
    for i in range(1, n):
        if pre < mas[i]:
            fre[i + 1] = fre[i] + mas[i] - pre
            sre[i + 1] = sre[i]
        else:
            fre[i + 1] = fre[i]
            sre[i + 1] = sre[i] + pre - mas[i]
        pre = mas[i]
    m = int(file.readline().rstrip())
    for _ in range(m):
        s, f = map(int, file.readline().rstrip().split())
        if s < f:
            print(fre[f] - fre[s])
        else:
            print(sre[s] - sre[f])

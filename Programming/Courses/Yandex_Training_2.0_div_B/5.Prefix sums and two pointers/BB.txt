with open('input.txt', 'r') as fin:
    n = int(fin.readline())
    mas = list(map(int, fin.readline().split()))
    mas.append(0)
    for i in range(n):
        mas[-(i + 1)] = mas[-(i + 2)]
    mas[0] = 0
    for i in range(n):
        mas[i + 1] = mas[i] + mas[i+1]
    diff = float('-inf')
    ma = mas[-1]
    for i in range(n):
        if mas[-(i + 2)] > ma:
            ma = mas[-(i + 2)]
        else:
            diff = max(diff, ma - mas[-(i + 2)])
    if diff == float('-inf'):
        masi = (mas[i+1] - mas[i] for i in range(n))
        diff = max(masi)
    print(diff)
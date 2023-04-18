with open('input.txt', 'r') as fin:
    n, q = map(int, (fin.readline().rstrip()).split())
    mas = list(map(int, fin.readline().rstrip().split()))
    perf = [0] * (n + 1)
    for i in range(n):
        perf[i + 1] = perf[i] + mas[i]
    for i in range(q):
        l, r = map(int, fin.readline().split())
        print(perf[r] - perf[l - 1])

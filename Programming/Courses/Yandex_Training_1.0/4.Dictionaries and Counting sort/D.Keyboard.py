n = int(input())
mas = list(map(int, input().split()))
di = {i + 1: mas[i] for i in range(n)}
n = int(input())
mas = map(int, input().split())
for ma in mas:
    di[ma] -= 1
for key in di:
    print('YES' if di[key] < 0 else 'NO')
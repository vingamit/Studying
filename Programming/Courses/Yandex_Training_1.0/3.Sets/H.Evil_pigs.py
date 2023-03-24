ans = set()
with open('input.txt', 'r', encoding='UTF-8') as fil:
    n = int(fil.readline().rstrip())
    for i in range(n):
        a, b = map(int, fil.readline().rstrip().split())
        ans.add(a)
print(len(ans))
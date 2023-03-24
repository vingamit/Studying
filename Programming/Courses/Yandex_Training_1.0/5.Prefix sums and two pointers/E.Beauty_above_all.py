with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().rstrip().split())
    mas = list(map(int, file.readline().rstrip().split()))
    di = {i + 1: 0 for i in range(k)}
    se = set()
    i = 0
    j = 0
    ans = []
    while i < n:
        while j < n and len(se) < k:
            se.add(mas[j])
            di[mas[j]] += 1
            j += 1
        if len(se) == k:
            ans.append((i + 1, j))
        di[mas[i]] -= 1
        if di[mas[i]] == 0:
            se.remove(mas[i])
        i += 1
    ans.sort(key=lambda x: x[1] - x[0])
    print(*ans[0])

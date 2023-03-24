num = list(map(int, input().split()))
if len(num) < 3:
    print(0)
else:
    res = 0
    for i in range(1, len(num) - 1):
        if num[i] > num[i - 1] and num[i] > num[i + 1]:
            res += 1
    print(res)
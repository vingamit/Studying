n, k = map(int, input().split())
mas = list(map(int, input().split()))
res = 0
left = 0
curr = 0

for num in mas:
    curr += num
    while curr > k:
        curr -= mas[left]
        left += 1

    if curr == k:
        res += 1
print(res)

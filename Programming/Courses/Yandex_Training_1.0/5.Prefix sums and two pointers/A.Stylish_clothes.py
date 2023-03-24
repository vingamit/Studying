n = int(input())
shi = list(map(int, input().split()))
m = int(input())
pan = list(map(int, input().split()))
i = 0
j = 0
bi = 0
bj = 0
diff = float('inf')
while i < len(shi) and j < len(pan):
    if shi[i] == pan[j]:
        bi, bj = i, j
        break
    new_res = abs(shi[i] - pan[j])
    if new_res < diff:
        bi, bj = i, j
        diff = new_res
    if shi[i] > pan[j]:
        j += 1
    else:
        i += 1
print(shi[bi], pan[bj])
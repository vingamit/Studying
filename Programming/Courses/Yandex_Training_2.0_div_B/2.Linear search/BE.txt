numb = int(input())
lst = list(map(int, input().split()))
summ = 0
maxm = 0
for i in range(numb):
    summ += lst[i]
    if lst[i] > maxm:
        maxm = lst[i] 
print(summ-maxm)
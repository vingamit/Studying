lst = list(map(int, input().split()))
def max_dist(lis):
    n = len(lis)
    mini = 10
    maxi = 0
    for i in range(n):
        if lis[i]==1:
            for j in range(n):
                if lst[j]==2 :
                    if mini > abs(j-i):
                        mini = abs(j-i)
            if mini> maxi:
                maxi = mini
        mini = 10
    return maxi
print(max_dist(lst))
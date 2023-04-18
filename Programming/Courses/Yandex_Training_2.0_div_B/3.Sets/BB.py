lst = list(map(int,input().split()))
numb = set()
for i in range(len(lst)):
    if lst[i] not in numb:
        print("NO")
        numb.add(lst[i])
    else:
        print("YES")
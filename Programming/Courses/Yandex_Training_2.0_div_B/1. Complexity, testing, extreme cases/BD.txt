n = int(input())
lst = list(map(int,input().split()))
if n%2==0:
    print(lst[n//2-1])
else:
    print(lst[n//2])
length , blo = map(int, input().split())
lst = list(map(int, input().split()))
a,b = lst[0],lst[blo-1]
k,c = 0,lst[blo-1]
t = length//2
d = length / 2
if length%2==0:
    for i in range(blo):
        if lst[i] >= a and lst[i] < t:
            a = lst[i]
        if lst[i] <=b and lst[i] >=t:
            b = lst[i]
    print(a,b)
else:
    for i in range(blo):
        if lst[i] >= k and lst[i] <= d:
            k = lst[i]
        if lst[i] <=c and lst[i] >=d:
            c = lst[i]
    if k == t or c == t:
        print(t)
    elif k==c:
        print(k)
    else:
        print(k,c)
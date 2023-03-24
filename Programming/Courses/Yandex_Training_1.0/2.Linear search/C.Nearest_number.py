le = int(input())
mas = list(map(int, input().split()))
target = int(input())
diff = 20002
d = None
for i in mas:
    if abs(target - i) < diff:
        diff = abs(target - i)
        d = i
print(d)

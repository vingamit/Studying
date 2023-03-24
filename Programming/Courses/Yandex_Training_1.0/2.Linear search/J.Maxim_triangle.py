left = 30
right = 4000
n = int(input())
prev = float(input())
for i in range(n - 1):
    f, s = input().rstrip().split()
    now = float(f)
    if abs(now - prev) < 10**(-6):
        continue
    if s == 'closer':
        if now > prev:
            left = max(left, (now + prev) / 2)
        else:
            right = min(right, (now + prev) / 2)
    else:
        if now < prev:
            left = max(left, (now + prev) / 2)
        else:
            right = min(right, (now + prev) / 2)
    prev = now
print(left, right)
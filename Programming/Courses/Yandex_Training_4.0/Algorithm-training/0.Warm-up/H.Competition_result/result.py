a, b, n = (int(input()) for _ in range(3))
re = b // n + (1 if b % n > 0 else 0)
if a > re:
    print("Yes")
else:
    print("No")
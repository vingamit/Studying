a = int(input())
b = int(input())
m = int(input())
n = int(input())
min_a_time = m + (m - 1) * a
max_a_time = m + (m + 1) * a
min_b_time = n + (n - 1) * b
max_b_time = n + (n + 1) * b
left = max(min_a_time, min_b_time)
right = min(max_a_time, max_b_time)
if left > right:
    print(-1)
else:
    print(left, right)
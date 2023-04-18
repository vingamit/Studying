from math import pi


with open('input.txt', 'r') as file:
    n = int(file.readline().rstrip())
    rmi = 0
    rma = 1e6
    events = []
    for i in range(n):
        r1, r2, ph1, ph2 = map(float, file.readline().rstrip().split())
        rmi = max(rmi, r1)
        rma = min(rma, r2)
        if ph1 > ph2:
            events.append((0, -1))
            events.append((ph2, 1))
            events.append((ph1, -1))
            events.append((2 * pi, 1))
        else:
            events.append((ph1, -1))
            events.append((ph2, 1))
events.sort()
now = 0
le = len(events)
angle = 0
for i in range(le):
    if now == n:
        angle += events[i][0] - events[i - 1][0]
    event = events[i]
    if event[1] == -1:
        now += 1
    else:
        now -= 1
area = (rma * rma - rmi * rmi) * angle / 2
print(area)

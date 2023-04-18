n, mu = map(int, input().split())
mas = list(map(int, input().split()))
mas.sort()


def left(num):
    le = -1
    r = len(mas)
    while r - le > 1:
        m = (le + r) // 2
        if mas[m] < num:
            le = m
        else:
            r = m
    return le


def right(num):
    le = -1
    r = len(mas)
    while r - le > 1:
        m = (le + r) // 2
        if mas[m] <= num:
            le = m
        else:
            r = m
    return le


for _ in range(mu):
    lef, rig = map(int, input().split())
    print((right(rig) - left(lef)), end=' ')

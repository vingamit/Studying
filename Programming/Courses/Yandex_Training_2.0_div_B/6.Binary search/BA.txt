nu = int(input())
mas = list(map(int, input().split()))
mas.sort()


def bi_se(n):
    le = 0
    r = len(mas) - 1
    while le <= r:
        m = (le + r) // 2
        if mas[m] < n:
            le = m + 1
        elif mas[m] > n:
            r = m - 1
        else:
            return True
    return False


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


k = int(input())
for i in range(k):
    lef, rig = map(int, input().split())
    print(right(rig) - left(lef), end=' ')

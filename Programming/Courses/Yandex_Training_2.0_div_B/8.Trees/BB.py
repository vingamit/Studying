with open('input.txt', 'r') as file:
    n = int(file.readline().rstrip())
    di = dict()
    for _ in range(n - 1):
        son, fat = file.readline().rstrip().split()
        di[son] = fat
    for line in file:
        fi, se = line.rstrip().split()
        ans1 = set()
        ans2 = set()
        tr = fi
        while tr in di:
            ans1.add(di[tr])
            tr = di[tr]
        tr = se
        while tr in di:
            ans2.add(di[tr])
            tr = di[tr]
        if fi in ans2:
            print('1', end=' ')
        elif se in ans1:
            print('2', end=' ')
        else:
            print('0', end=' ')


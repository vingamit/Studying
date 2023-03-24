with open('input.txt', 'r') as file:
    n, k = map(int, file.readline().rstrip().split())
    mas = list(map(int, file.readline().rstrip().split()))
    targets = list(map(int, file.readline().rstrip().split()))


    def bis(num):
        le = 0
        ri = n - 1
        while le <= ri:
            mi = (le + ri) // 2
            if mas[mi] > num:
                ri = mi - 1
            elif mas[mi] < num:
                le = mi + 1
            else:
                return 'YES'
        return 'NO'


    for target in targets:
        print(bis(target))

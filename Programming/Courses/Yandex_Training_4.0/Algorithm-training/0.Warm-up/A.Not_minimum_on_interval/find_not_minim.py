n, m = map(int, input().split())
mas = list(map(int, input().split()))
for _ in range(m):
    l, r = map(int, input().split())
    surmas = mas[l: r + 1]
    length = len(set(surmas))
    if length == 1:
        print("NOT FOUND")
    else:
        fi, se = float("inf"), float("inf")
        for el in surmas:
            if el < fi:
                fi, se = el, fi
            elif el < se and el != fi:
                se = el
        print(se)
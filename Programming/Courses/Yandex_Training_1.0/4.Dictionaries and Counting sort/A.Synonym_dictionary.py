n = int(input())
di = {}
for i in range(n):
    fi, se = input().split()
    di[fi] = se
    di[se] = fi
fin = input()
print(di[fin])
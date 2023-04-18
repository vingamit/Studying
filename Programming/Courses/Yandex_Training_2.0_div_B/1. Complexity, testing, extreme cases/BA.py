x = int(input())
y = int(input())
z = int(input())
if y == 0:
    if x != 0:
        print(3)
    else:
        print(z)
elif y == 1:
    print(z)
elif y == 4:
    if x!=0:
        print(3)
    else:
        print(4)
elif y == 6:
    print(0)
elif y == 7:
    print(1)
else:
    print(y)
      
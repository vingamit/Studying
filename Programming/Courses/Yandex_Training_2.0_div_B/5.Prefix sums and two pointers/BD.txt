inpu = input()
cou = 0
nar = 0
for inp in inpu:
    if inp == ')':
        cou -= 1
    else:
        cou += 1
    if cou == -1:
        print('NO')
        nar = 1
        break
if nar == 0 and cou == 0:
    print('YES')
elif nar == 0 and cou > 0:
    print('NO')
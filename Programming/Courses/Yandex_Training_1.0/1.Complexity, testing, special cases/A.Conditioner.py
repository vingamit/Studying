troom, tcond = map(int, input().split())
a = input()
troom = int(troom)
tcond = int(tcond)
range = troom - tcond
if -50 > (troom or tcond) > 50:
    a = ''
if a == 'freeze' and range > 0:
    print(tcond)
elif a == 'freeze' and range <= 0:
    print(troom)
if a == 'heat' and range < 0:
    print(tcond)
elif a == 'heat' and range >= 0:
    print(troom)
if a == 'auto':
    print(tcond)
if a == 'fan':
    print(troom)

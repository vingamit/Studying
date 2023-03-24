x, y, z = map(str, input().split())
num = input()
det = set()
ket = set()
det.add(x)
det.add(y)
det.add(z)
cou = 0
for i in range(len(num)):
    if num[i] not in det and num[i] not in ket:
        cou +=1
        ket.add(num[i])
print(cou)
    
    
n = int(input())
k = 0
di = {}
messages = []
while k < n:
    nu = int(input())
    if nu == 0:
        them = input()
        mes = input()
        di[them] = 1
        messages.append((mes, them))
        k += 1
    else:
        mes = input()
        prev = messages[nu - 1]
        messages.append((mes, prev[1]))
        di[prev[1]] += 1
        k += 1
maxi = 0
for key in di:
    if di[key] > maxi:
        maxi = di[key]
for key in di:
    if di[key] == maxi:
        print(key)
        break
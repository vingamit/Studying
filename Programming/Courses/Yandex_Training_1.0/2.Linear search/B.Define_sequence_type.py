mas = [False, False, False]
with open('input.txt', 'r') as file:
    i = 0
    flag = True
    while flag:
        if i == 0:
            i = 1
            nu = int(file.readline().rstrip())
            if nu == -2000000000:
                flag = False
        prev = nu
        nu = int(file.readline().rstrip())
        if nu == -2000000000:
            break
        diff = nu - prev
        if diff > 0:
            mas[2] = True
        elif diff < 0:
            mas[0] = True
        else:
            mas[1] = True
if mas == [0, 1, 0]:
    print('CONSTANT')
elif mas == [0, 0, 1]:
    print('ASCENDING')
elif mas == [0, 1, 1]:
    print('WEAKLY ASCENDING')
elif mas == [1, 0, 0]:
    print('DESCENDING')
elif mas == [1, 1, 0]:
    print('WEAKLY DESCENDING')
else:
    print('RANDOM')
k=1
lst = []
while k!=0:
    k = int(input())
    if k==0:
        break
    lst.append(k)
def max_of_seq(x):
    mini = 0
    for i in range(len(x)):
        if lst[i] > mini:
            mini = lst[i]
            k = 1
        elif lst[i] == mini:
            k+=1
    return k
print(max_of_seq(lst))
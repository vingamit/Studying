poli = str(input())
def polin(lst):
    n = len(lst)
    k = 0 
    for i in range(n//2):
        if poli[i] != poli[n -1 -i]:
            k += 1
    return k
print(polin(poli))
di = {}
with open('input.txt', 'r', encoding='UTF-8') as fin:
    n = int(fin.readline().rstrip())
    for i in range(n):
        word = fin.readline().rstrip()
        if word.lower() not in di:
            di[word.lower()] = [word]
        else:
            di[word.lower()].append(word)
    text = fin.readline().rstrip().split()
res = 0
for tex in text:
    if tex.lower() in di:
        if tex not in di[tex.lower()]:
            res += 1
    else:
        su = 0
        for alp in tex:
            if alp.isupper():
                su += 1
        if su != 1:
            res += 1
print(res)
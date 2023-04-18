wordcnt = {}
with open('input.txt', 'r', encoding='utf8') as fin:
    for line in fin:
        words = line.split()
        for word in words:
            wordcnt[word] = wordcnt.get(word, 0) + 1
ans = []
for word in wordcnt:
    ans.append((-wordcnt[word], word))
ans.sort()
for cnt, word in ans:
    print(word)
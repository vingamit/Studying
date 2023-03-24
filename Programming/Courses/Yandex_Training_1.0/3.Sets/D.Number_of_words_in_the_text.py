words = set()
with open('input.txt', 'r', encoding='UTF-8') as fil:
    for line in fil:
        line = line.rstrip().split()
        for word in line:
            words.add(word)
print(len(words))
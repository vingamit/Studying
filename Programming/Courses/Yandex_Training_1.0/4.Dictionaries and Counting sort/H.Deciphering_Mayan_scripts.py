def makeDict(s):
    sDict = {}
    for c in s:
        if c not in sDict:
            sDict[c] = 0
        sDict[c] += 1
    return sDict


def matchDicst(dict1, dict2):
    matches = 0
    for c in dict1:
        if c in dict2 and dict1[c] == dict2[c]:
            matches += 1
    return matches


def modifyDict(sDict, wDict, symbol, countModifier):
    ans = 0
    if symbol not in sDict:
        sDict[symbol] = 0
    if symbol in wDict and sDict[symbol] == wDict[symbol]:
        ans -= 1
    sDict[symbol] += countModifier
    if symbol in wDict and sDict[symbol] == wDict[symbol]:
        ans = 1
    return ans


lenW, lenS = map(int, input().split())
w = input()
s = input()
wDict = makeDict(w)
sDict = makeDict(s[:lenW])
matchingLetters = matchDicst(wDict, sDict)
occurrences = 0
if matchingLetters == len(wDict):
    occurrences += 1
for i in range(lenW, lenS):
    matchingLetters += modifyDict(sDict, wDict, s[i - lenW], -1)
    matchingLetters += modifyDict(sDict, wDict, s[i], +1)
    if matchingLetters == len(wDict):
        occurrences += 1
print(occurrences)

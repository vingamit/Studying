bracket = list(input())
di_bra = {')': '(', '}': '{', ']': '['}
stack = []
flag = True
for ele in bracket:
    if ele in di_bra.values():
        stack.append(ele)
    elif stack and stack[-1] == di_bra[ele]:
        stack.pop()
    else:
        flag = False
        break

if flag and not stack:
    print("yes")
else:
    print("no")
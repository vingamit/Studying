with open('input.txt', 'r') as file:
    n = int(file.readline().rstrip())
    di = dict()
    for _ in range(n - 1):
        son, fat = file.readline().rstrip().split()
        if fat not in di:
            di[fat] = [None, [], 0]
        if son not in di:
            di[son] = [None, [], 0]
        di[fat][1].append(son)
        di[son][0] = fat
    ancestor = None
    for key in di:
        if di[key][0] is None:
            ancestor = key

    def dfs(kyy, a=0):
        di[kyy][2] = a
        for desc in di[kyy][1]:
            dfs(desc, a + 1)

    dfs(ancestor)
    for line in file:
        fr, to = line.rstrip().split()
        mi = min(di[fr][2], di[to][2])
        while di[fr][2] != mi:
            fr = di[fr][0]
        while di[to][2] != mi:
            to = di[to][0]
        while fr != to:
            fr = di[fr][0]
            to = di[to][0]
        print(fr)


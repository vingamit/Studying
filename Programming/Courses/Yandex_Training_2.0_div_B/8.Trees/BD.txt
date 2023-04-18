from sys import setrecursionlimit


setrecursionlimit(100000)
n = int(input())
mas = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    mas[a].append(b)
    mas[b].append(a)
visited = [False for _ in range(n)]
dist = [0 for _ in range(n)]


def dfs(num):
    visited[num - 1] = True
    best = 1
    max1 = -1
    max2 = -1
    dist[num - 1] = 1
    for neigh in mas[num]:
        if not visited[neigh - 1]:
            best = max(dfs(neigh), best)
            if dist[neigh - 1] > max1:
                max2 = max1
                max1 = dist[neigh - 1]
            elif dist[neigh - 1] > max2:
                max2 = dist[neigh - 1]
    best = max(best, max1 + 1)
    best = max(best, max1 + max2 + 1)
    dist[num - 1] = max(dist[num - 1], max1 + 1)
    return best


print(dfs(1))

def dfs(v):
    visited[v] = 1
    if len(tree[v]) == 0:
        d[v][0] = 0
        d[v][1] = 1
    else:
        for i in tree[v]:
            if not visited[i]:
                dfs(i)
                d[v][0] += d[i][1]
                d[v][1] += min(d[i])
        d[v][1] += 1

from sys import stdin, setrecursionlimit
setrecursionlimit(10**9)
n = int(stdin.readline())
tree = {i: [] for i in range(1, n+1)}
for i in range(n-1):
    u, v = map(int, stdin.readline().split())
    tree[u].append(v)
    tree[v].append(u)
visited = {i: 0 for i in range(1, n+1)}
d = [[0]*2 for i in range(n+1)]
dfs(1)
print(min(d[1]))
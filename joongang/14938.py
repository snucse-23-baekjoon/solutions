def fw():
    d = [[float('inf')]*(n+1) for i in range(n+1)]
    for i in range(1, n+1):
        d[i][i] = 0
    for i in graph:
        for j, k in graph[i]:
            d[i][j] = k
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])
    return d

from sys import stdin
n, m, r = map(int, stdin.readline().split())
item = [0] + list(map(int, stdin.readline().split()))
graph = {i: [] for i in range(1, n+1)}
for _ in range(r):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append((y, z))
    graph[y].append((x, z))
d = fw()
s = 0
for i in range(1, n+1):
    tmp = 0
    for j in range(1, n+1):
        if d[i][j] <= m:
            tmp += item[j]
    s = max(s, tmp)
print(s)
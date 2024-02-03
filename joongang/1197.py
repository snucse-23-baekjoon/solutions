def find(x):
    if uf[x] == x:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin
from collections import deque
v, e = map(int, stdin.readline().split())
graph = [list(map(int, stdin.readline().split())) for i in range(e)]
graph.sort(key=lambda x: x[2])
graph = deque(graph)
uf = {i: i for i in range(1, v+1)}
ans = 0
for x, y, z in graph:
    if find(x) != find(y):
        ans += z
        union(x, y)
print(ans)
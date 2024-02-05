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
n, m = map(int, stdin.readline().split())
E = [list(map(int, stdin.readline().split())) for i in range(m)]
E.sort(key=lambda x: x[2])
uf = {i: i for i in range(1, n+1)}
mst = []
for x, y, z in E:
    if find(x) != find(y):
        mst.append((x, y, z))
        union(x, y)
M = 0
ans = 0
for x, y, z in mst:
    ans += z
    M = max(M, z)
print(ans-M)
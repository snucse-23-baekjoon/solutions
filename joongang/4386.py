def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin
import math
n = int(stdin.readline())
stars = [list(map(float, stdin.readline().split())) for i in range(n)]
E = []
for i in range(n):
    for j in range(i+1, n):
        dist = math.sqrt((stars[i][0]-stars[j][0])**2 + (stars[i][1]-stars[j][1])**2)
        E.append((i, j, dist))
E.sort(key = lambda x: x[2])
uf = {i: i for i in range(n)}
mst = []
cnt = 0
idx = 0
while cnt < n-1:
    x, y, z = E[idx]
    if find(x) != find(y):
        mst.append((x, y, z))
        union(x, y)
        cnt += 1
    idx += 1
s = 0
for x, y, z in mst:
    s += z
print(round(s, 2))
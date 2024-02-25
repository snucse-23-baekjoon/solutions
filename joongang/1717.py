def find(x):
    if x != uf[x]:
        uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin
n, m = map(int, stdin.readline().split())
uf = {i: i for i in range(n+1)}
for _ in range(m):
    op, x, y = map(int, stdin.readline().split())
    if op == 0:
        union(x, y)
    else:
        if find(x) == find(y):
            print('yes')
        else:
            print('no')
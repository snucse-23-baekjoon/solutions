def find(x):
    if x != uf[x]:
        uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin, setrecursionlimit
setrecursionlimit(10**6)
n, m = map(int, stdin.readline().split())
E = [list(map(int, stdin.readline().split())) for i in range(m)]
uf = {i: i for i in range(n)}
for i in range(m):
    x, y = E[i]
    if find(x) == find(y):
        print(i+1)
        exit(0)
    else:
        union(x, y)
print(0)
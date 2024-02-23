def find(x):
    if x != uf[x]:
        uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin, setrecursionlimit
setrecursionlimit(10**5)
n, m, k = map(int, stdin.readline().split())
candy = list(map(int, stdin.readline().split()))
E = [list(map(int, stdin.readline().split())) for i in range(m)]
uf = {i: i for i in range(1, n+1)}
for x, y in E:
    union(x, y)
d = {}
for i in range(1, n+1):
    find(i)
    if uf[i] not in d:
        d[uf[i]] = [1, candy[i-1]]
    else:
        d[uf[i]][0] += 1
        d[uf[i]][1] += candy[i-1]
popul_candy = list(d.values())
dp = [0]*k
for p, c in popul_candy:
    for i in range(k-1, p-1, -1):
        dp[i] = max(dp[i], dp[i-p]+c)
print(max(dp))
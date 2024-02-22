import sys


def search(vertex):
    next_level = []
    for j in range(N):
        if G[vertex][j] == 1 and V[j] == 0:
            V[j] = 1
            next_level.append(j)
    if next_level:
        for v in next_level:
            search(v)


N, M = map(int, sys.stdin.readline().split())
V = [0] * N
G = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    G[a][b], G[b][a] = 1, 1
ans = 0
for i in range(N):
    if not V[i]:
        ans += 1
        search(i)
print(ans)

import sys


def search(vertex):
    newly_found = False
    for i in range(N):
        if G[vertex][i] == 1 and i not in visited:
            newly_found = True
            for j in range(N):
                if G[i][j] == 1:
                    G[vertex][j] = 1
            visited.append(i)
    if newly_found:
        search(vertex)


N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
G = [[0] * N for _ in range(N)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    G[a][b], G[b][a] = 1, 1
visited = []
search(0)
cnt = 0
for k in range(1, N):
    if G[0][k] == 1:
        cnt += 1
print(cnt)

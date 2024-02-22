import sys


def search(vertex, visited):
    found = False
    for j in range(N):
        if G[vertex][j] and j not in visited:
            found = True
            visited.add(j)
            for k in range(N):
                if G[j][k]:
                    G[vertex][k] = 1
    if found:
        search(vertex, visited)


N = int(sys.stdin.readline())
G = []
for _ in range(N):
    G.append(list(map(int, sys.stdin.readline().split())))
for i in range(N):
    search(i, set())
for line in G:
    print(*line)


from sys import stdin
stdin = open("../input.txt", 'r')

def dfs(u):
    if visited[u]: return 0
    visited[u] = 1
    for v in graph[u]:
        w = selected[v]
        if w == -1 or dfs(w):
            selected[v] = u; return 1
    return 0

for _ in range(int(stdin.readline())):
    N, M = map(int, stdin.readline().split())
    graph = [[] for _ in range(N)]
    for _ in range(M):
        u, v = map(int, stdin.readline().split())
        graph[u].append(v)

    matches = 0
    selected = [-1] * N
    for i in range(N):
        visited = [0] * N
        matches += dfs(i)
    print(matches)

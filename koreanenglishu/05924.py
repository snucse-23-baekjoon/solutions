from sys import stdin
stdin = open("../input.txt", 'r')

def dfs(u):
    if visited[u]: return 0
    visited[u] = True
    for v in graph[u]:
        if selected[v] < 0 or dfs(selected[v]):
            selected[v] = u; return 1
    return 0

horizontal, vertical = list(), list()
N = int(stdin.readline())
for _ in range(N):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    if (x1, y1) > (x2, y2): x1, y1, x2, y2 = x2, y2, x1, y1
    if x1 == x2: vertical.append((x1, y1, x2, y2))
    if y1 == y2: horizontal.append((x1, y1, x2, y2))

H, V = len(horizontal), len(vertical)
graph = [[] for _ in range(H)]
for h in range(H):
    x1, y1, x2, y2 = horizontal[h]
    for v in range(V):
        x3, y3, x4, y4 = vertical[v]
        if x1 <= x3 <= x2 and y3 <= y1 <= y4:
            graph[h].append(v)

count = 0
selected = [-1] * V
for h in range(H):
    visited = [False] * H
    count += dfs(h)

print(N - count)

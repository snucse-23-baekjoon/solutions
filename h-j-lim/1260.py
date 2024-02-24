import sys


def dfs(node, visited, component):
    visited.append(node)
    component.append(node)
    for adjacent in adjacency_list[node]:
        if adjacent not in visited:
            dfs(adjacent, visited, component)


def bfs(current_level, visited, component):
    component.extend(current_level)
    next_level = []
    for node in current_level:
        for adjacent in adjacency_list[node]:
            if adjacent not in visited:
                next_level.append(adjacent)
                visited.append(adjacent)
    if next_level:
        bfs(next_level, visited, component)


N, M, V = map(int, sys.stdin.readline().split())
adjacency_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in adjacency_list[a]:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
for i in range(1, N + 1):
    adjacency_list[i].sort()
res = []
dfs(V, [], res)
print(*res)
res = []
bfs([V], [V], res)
print(*res)

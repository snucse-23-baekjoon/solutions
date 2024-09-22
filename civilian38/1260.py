import sys
from collections import deque

graph = dict()
n, m, v = map(int, sys.stdin.readline().split())
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if graph.get(a):
        graph[a].add(b)
    else:
        graph[a] = set([b])
    if graph.get(b):
        graph[b].add(a)
    else:
        graph[b] = set([a])
        
if graph.get(v):
    dfs = list()
    queue = deque()
    queue.append(v)
    while queue:
        node = queue.pop()
        if node not in dfs:
            dfs.append(node)
            for item in reversed(sorted(list(graph[node]))):
                queue.append(item)
    print(*dfs)

    bfs = list()
    stack = deque()
    stack.append(v)
    while stack:
        node = stack.popleft()
        if node not in bfs:
            bfs.append(node)
            for item in sorted(list(graph[node])):
                stack.append(item)
    print(*bfs)
else:
    print(v)
    print(v)
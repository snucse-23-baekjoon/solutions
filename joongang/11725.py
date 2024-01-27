def bfs():
    visited = {i: 0 for i in range(1, n+1)}
    parent = {i: 0 for i in range(2, n+1)}
    visited[1] = 1
    q = deque([1])
    while q:
        cur = q.popleft()
        for i in tree[cur]:
            if not visited[i]:
                visited[i] = 1
                parent[i] = cur
                q.append(i)
    return parent
    
from sys import stdin
from collections import deque
n = int(stdin.readline())
tree = {i: [] for i in range(1, n+1)}
for _ in range(n-1):
    x, y = map(int, stdin.readline().split())
    tree[x].append(y)
    tree[y].append(x)
parent = bfs()
for i in range(2, n+1):
    print(parent[i])
def dfs(n, E, v):
    visited = {i: 0 for i in range(1, n+1)}
    visited[v] = 1
    print(v, end=' ')
    def search(E, v):
        for i in E[v]:
            if not visited[i]:
                print(i, end=' ')
                visited[i] = 1
                search(E, i)
    search(E, v)
    
def bfs(n, E, v):
    visited = {i: 0 for i in range(1, n+1)}
    visited[v] = 1
    queue = [v]
    while queue:
        for i in E[queue[0]]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
        print(queue.pop(0))
    
from sys import stdin
n, m, v = map(int, stdin.readline().split())
E = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    E[x].append(y)
    E[y].append(x)
for i in range(1, n+1):
    E[i].sort()
dfs(n, E, v)
print()
bfs(n, E, v)
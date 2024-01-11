def bfs(E):
    n = len(E)
    visited = [0 for i in range(n)]
    visited[0] = 1
    queue = [1]
    while queue:
        for i in E[queue[0]]:
            if not visited[i-1]:
                queue.append(i)
                visited[i-1] = 1
        queue.pop(0)
    return visited.count(1)

from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
E = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    E[x].append(y)
    E[y].append(x)
print(bfs(E)-1)
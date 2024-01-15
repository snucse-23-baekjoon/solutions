def bfs(E, v):
    visited[v] = 1
    queue = [v]
    while queue:
        for i in E[queue[0]]:
            if not visited[i]:
                visited[i] = 1
                queue.append(i)
        queue.pop(0)

from sys import stdin
n, m = map(int, stdin.readline().split())
E = {i: [] for i in range(n)}
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    E[x-1].append(y-1)
    E[y-1].append(x-1)
visited = {i: 0 for i in range(n)}
ans = 0
for i in range(n):
    if not visited[i]:
        ans += 1
        bfs(E, i)
print(ans)      
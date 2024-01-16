def bfs(E, v):
    visited = {i: 0 for i in range(1, 100)}
    queue = deque([v])
    while queue:
        before = queue[0]
        for i in range(1, 7):
            after = before + i
            if after in E:
                after = E[after]
            if after == 100:
                return visited[before] + 1
            if not visited[after]:
                visited[after] = visited[before] + 1
                queue.append(after)
        queue.popleft()

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
E = dict()
for _ in range(n+m):
    x, y = map(int, stdin.readline().split())
    E[x] = y
print(bfs(E, 1))
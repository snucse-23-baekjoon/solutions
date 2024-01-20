def bfs(i, j):
    visited[i][j] = 0
    queue = deque([(i, j)])
    while queue:
        a = queue[0][0]
        b = queue[0][1]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m and not visited[x][y] and lst[x][y]:
                visited[x][y] = visited[a][b] + 1
                queue.append((x, y))
        queue.popleft()

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
ans = [[0]*m for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0]*m for i in range(n)]
try:
    for i in range(n):
        for j in range(m):
            if lst[i][j] == 2:
                bfs(i, j)
                visited[i][j] = 0
                raise
except:
    pass
for i in range(n):
    for j in range(m):
        if lst[i][j] == 1 and not visited[i][j]:
            visited[i][j] = -1
        print(visited[i][j], end=' ')
    print()
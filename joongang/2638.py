def bfs():
    visited = [[0]*m for i in range(n)]
    visited[0][0] = 1
    q = deque([(0, 0)])
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<m:
                if lst[x][y]:
                    visited[x][y] += 1
                elif not visited[x][y]:
                    visited[x][y] = 1
                    q.append((x, y))
    return visited

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
t = 0
while 1:
    visited = bfs()
    chk = 0
    for i in range(n):
        for j in range(m):
            if visited[i][j] >= 2:
                chk = 1
                lst[i][j] = 0
    if chk:
        t += 1
    else:
        break
print(t)
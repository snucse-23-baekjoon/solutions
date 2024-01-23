def bfs():
    visited = [[[0]*m for i in range(n)] for j in range(2)]
    visited[0][0][0] = 1
    q = deque([(0, 0, 0)])
    while q:
        chk, a, b = q.popleft()
        if (a, b) == (n-1, m-1):
            if chk:
                return visited[1][a][b]
            if not chk:
                return visited[0][a][b]
            return min(visited[0][a][b], visited[1][a][b])
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<m:
                if chk:
                    if (not visited[1][x][y] or visited[1][x][y] > visited[1][a][b] + 1) and not lst[x][y]:
                        visited[1][x][y] = visited[1][a][b] + 1
                        q.append((1, x, y))
                else:
                    if not lst[x][y]:
                        if not visited[0][x][y]:
                            visited[0][x][y] = visited[0][a][b] + 1
                            q.append((0, x, y))
                    else:
                        if not visited[1][x][y] or visited[1][x][y] > visited[0][a][b] + 1:
                            visited[1][x][y] = visited[0][a][b] + 1
                            q.append((1, x, y))
    return -1                   

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
lst = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs())
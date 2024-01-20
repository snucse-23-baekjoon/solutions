def bfs(i, j):
    visited = [[0]*m for _ in range(n)]
    visited[i][j] = 1
    queue = deque([(i, j)])
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    result = 0
    while queue:
        a = queue[0][0]
        b = queue[0][1]
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m and not visited[x][y] and lst[x][y] != 'X':
                visited[x][y] = 1
                queue.append((x, y))
                if lst[x][y] == 'P':
                    result += 1
        queue.popleft()
    if result:
        return result
    else:
        return 'TT'

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
lst = [stdin.readline().rstrip() for i in range(n)]
for i in range(n):
    for j in range(m):
        if lst[i][j] == 'I':
            print(bfs(i, j))
            exit(0)
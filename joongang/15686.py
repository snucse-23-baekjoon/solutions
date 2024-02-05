def dfs(chicken):
    visited = [[0]*n for i in range(n)]
    q = deque([])
    for i, j in chicken:
        visited[i][j] = 1
        q.append((i, j))
    d = 0
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<n and not visited[x][y]:
                visited[x][y] = visited[a][b] + 1
                q.append((x, y))
                if lst[x][y] == 1:
                    d += visited[a][b]
    return d

from sys import stdin
from collections import deque
from itertools import combinations
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
chickens = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if lst[i][j] == 2:
            chickens.append((i, j))
ans = float('inf')
for i in combinations(chickens, m):
    ans = min(ans, dfs(i))
print(ans)
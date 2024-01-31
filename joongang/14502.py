def dfs(virus, d1, d2, d3):
    global lst
    visited = [[0]*m for i in range(n)]
    for i, j in virus:
        visited[i][j] = 1
    lst[d1[0]][d1[1]] = 1
    lst[d2[0]][d2[1]] = 1
    lst[d3[0]][d3[1]] = 1
    q = deque(virus.copy())
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<m and not lst[x][y] and not visited[x][y]:
                visited[x][y] = visited[a][b] + 1
                q.append((x, y))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and not lst[i][j]:
                cnt += 1
    lst[d1[0]][d1[1]] = 0
    lst[d2[0]][d2[1]] = 0
    lst[d3[0]][d3[1]] = 0                
    return cnt

from sys import stdin
from collections import deque
from itertools import combinations
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
virus = []
empty = []
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            empty.append((i, j))
        elif lst[i][j] == 2:
            virus.append((i, j))
ans = 0
for d1, d2, d3 in combinations(empty, 3):
    ans = max(ans, dfs(virus, d1, d2, d3))
print(ans)
from sys import stdin
from collections import deque
m, n = map(int, stdin.readline().split())
queue = deque([])
lst = []
for i in range(n):
    lst.append(list(map(int, stdin.readline().split())))
    for j in range(m):
        if lst[i][j] == 1:
            queue.append((i, j))
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    a, b = queue.popleft()
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0<=x<n and 0<=y<m and lst[x][y] == 0:
            queue.append((x, y))
            lst[x][y] = lst[a][b] + 1
ans = 0            
for i in range(n):
    for j in range(m):
        if lst[i][j] == 0:
            print(-1)
            exit(0)
    ans = max(ans, max(lst[i]))
print(ans-1)
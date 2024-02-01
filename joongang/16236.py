def dfs(sx, sy):
    global lst, size, feed, cx, cy
    visited = [[0]*n for i in range(n)]
    visited[sx][sy] = 1
    q = deque([(sx, sy)])
    fish = []
    while q:
        a, b = q.popleft()
        if fish and visited[fish[0][0]][fish[0][1]] == visited[a][b]:
            fish.sort(key=lambda x: (x[0], x[1]))
            x, y = fish[0]
            lst[sx][sy] = 0
            lst[x][y] = 9
            cx = x
            cy = y
            feed += 1
            if feed == size:
                size += 1
                feed = 0
            return visited[x][y] - 1
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<n and 0<=y<n and not visited[x][y] and lst[x][y]<=size:
                if 0<lst[x][y]<size:
                    fish.append((x, y))
                visited[x][y] = visited[a][b] + 1
                q.append((x, y))
    return -1

from sys import stdin
from collections import deque
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
size = 2
feed = 0
ans = 0
try:
    for i in range(n):
        for j in range(n):
            if lst[i][j] == 9:
                cx = i
                cy = j
                raise
except:
    pass
while 1:
    t = dfs(cx, cy)
    if t == -1:
        break
    ans += t
print(ans)
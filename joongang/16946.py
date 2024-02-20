def bfs(i, j, g):
    q = deque([(i, j)])
    cnt = 1
    while q:
        a, b = q.popleft()
        for k in range(4):
            x = a + dx[k]
            y = b + dy[k]
            if 0<=x<n and 0<=y<m and not visited[x][y] and not lst[x][y]:
                visited[x][y] = 1
                group[x][y] = g
                q.append((x, y))
                cnt += 1
    return cnt%10

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
lst = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
group = [[0]*m for i in range(n)]
d = {0: 0}
g = 1
visited = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if not lst[i][j] and not visited[i][j]:
            visited[i][j] = 1
            group[i][j] = g
            d[g] = bfs(i, j, g)
            g += 1
ans = [[0]*m for i in range(n)]
for i in range(n):
    for j in range(m):
        if lst[i][j]:
            s = set()
            ans[i][j] += 1
            for k in range(4):
                x = i + dx[k]
                y = j + dy[k]
                if 0<=x<n and 0<=y<m and group[x][y] not in s:
                    ans[i][j] += d[group[x][y]]
                    ans[i][j] %= 10
                    s.add(group[x][y])
for i in range(n):
    for j in range(m):
        print(ans[i][j], end='')
    print()
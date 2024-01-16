def dfs(i, j, s, cnt):
    global ans
    if cnt == 4:
        ans = max(ans, s)
        return
    for k in range(4):
        x = i + dx[k]
        y = j + dy[k]
        if 0<=x<n and 0<=y<m and not visited[x][y]:
            visited[x][y] = 1
            dfs(x, y, s+lst[x][y], cnt+1)
            visited[x][y] = 0
            
def ex(i, j):
    global ans
    for k in range(4):
        tmp = lst[i][j]
        for l in range(4):
            if k != l:
                x = i + dx[l]
                y = j + dy[l]
                if not (0<=x<n and 0<=y<m):
                    tmp = 0
                    break
                tmp += lst[x][y]
        ans = max(ans, tmp)

from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
visited = [[0]*m for i in range(n)]
ans = 0
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
for i in range(n):
    for j in range(m):
        visited[i][j] = 1
        dfs(i, j, lst[i][j], 1)
        visited[i][j] = 0
        ex(i, j)
print(ans)
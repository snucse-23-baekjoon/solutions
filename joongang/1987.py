def dfs(a, b, cnt):
    global M
    M = max(M, cnt)
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0<=x<r and 0<=y<c and lst[x][y] not in visited:
            visited.add(lst[x][y])
            dfs(x, y, cnt+1)
            visited.remove(lst[x][y])

from sys import stdin
r, c = map(int, stdin.readline().split())
lst = [list(stdin.readline().rstrip()) for i in range(r)]
visited = set()
visited.add(lst[0][0])
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
M = 1
dfs(0, 0, 1)
print(M)
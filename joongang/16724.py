from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [list(stdin.readline().rstrip()) for i in range(n)]
visited = [[0]*m for i in range(n)]
ans = 0
cnt = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            x, y = i, j
            while not visited[x][y]:
                visited[x][y] = cnt
                if lst[x][y] == 'D':
                    x += 1
                elif lst[x][y] == 'R':
                    y += 1
                elif lst[x][y] == 'U':
                    x -= 1
                elif lst[x][y] == 'L':
                    y -= 1
            if visited[x][y] == cnt:
                ans += 1
            cnt += 1
print(ans)
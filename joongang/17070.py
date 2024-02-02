def dfs(x, y, r):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    if r==0:
        if y < n-1 and not lst[x][y+1]:
            dfs(x, y+1, 0)
            if x < n-1 and not lst[x+1][y] and not lst[x+1][y+1]:
                dfs(x+1, y+1, 2)
    elif r==1:
        if x < n-1 and not lst[x+1][y]:
            dfs(x+1, y, 1)
            if y < n-1 and not lst[x][y+1] and not lst[x+1][y+1]:
                dfs(x+1, y+1, 2)
    elif r==2:
        if y < n-1 and not lst[x][y+1]:
            dfs(x, y+1, 0)
        if x < n-1 and not lst[x+1][y]:
            dfs(x+1, y, 1)
        if x < n-1 and y < n-1 and not lst[x][y+1] and not lst[x+1][y] and not lst[x+1][y+1]:
            dfs(x+1, y+1, 2)

from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
ans = 0
dfs(0, 1, 0)
print(ans)
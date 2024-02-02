def f():
    tmp = [[0]*c for i in range(r)]
    tmp[cleaner[0]][0] = -1
    tmp[cleaner[1]][0] = -1
    for i in range(r):
        for j in range(c):
            if lst[i][j] > 0:
                tmp[i][j] += lst[i][j]
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0<=x<r and 0<=y<c and not (x in cleaner and y==0):
                        tmp[x][y] += lst[i][j] // 5
                        tmp[i][j] -= lst[i][j] // 5
    for i in range(cleaner[0]-1, 0, -1):
        tmp[i][0] = tmp[i-1][0]
    for i in range(c-1):
        tmp[0][i] = tmp[0][i+1]
    for i in range(cleaner[0]):
        tmp[i][c-1] =tmp[i+1][c-1]
    for i in range(c-1, 1, -1):
        tmp[cleaner[0]][i] = tmp[cleaner[0]][i-1]
    tmp[cleaner[0]][1] = 0
    for i in range(cleaner[1]+1, r-1):
        tmp[i][0] = tmp[i+1][0]
    for i in range(c-1):
        tmp[r-1][i] = tmp[r-1][i+1]
    for i in range(r-1, cleaner[1], -1):
        tmp[i][c-1] = tmp[i-1][c-1]
    for i in range(c-1, 1, -1):
        tmp[cleaner[1]][i] = tmp[cleaner[1]][i-1]
    tmp[cleaner[1]][1] = 0
    return tmp
                    

from sys import stdin
r, c, t = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(r)]
cleaner = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(r):
    if lst[i][0] == -1:
        cleaner.append(i)
for i in range(t):
    lst = f()
ans = 0
for i in range(r):
    ans += sum(lst[i])
print(ans + 2)
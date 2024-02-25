from sys import stdin
from copy import deepcopy
r, c, m = map(int, stdin.readline().split())
sharks = [list(map(int, stdin.readline().split())) for i in range(m)]
for i in range(m):
    sharks[i][0] -= 1
    sharks[i][1] -= 1
existence = [1 for i in range(m)]
board = [[-1]*c for i in range(r)]
for i in range(m):
    x, y, s, d, z = sharks[i]
    board[x][y] = i
ans = 0
for i in range(c):
    for j in range(r):
        if board[j][i] >= 0:
            ans += sharks[board[j][i]][4]
            existence[board[j][i]] = 0
            board[j][i] = -1
            break
    tmp = [[-1]*c for _ in range(r)]
    for j in range(m):
        if existence[j]:
            x, y, s, d, z = sharks[j]
            if d == 1:
                x -= s
            elif d == 2:
                x += s
            elif d == 3:
                y += s
            elif d == 4:
                y -= s
            while 1:
                if x < 0:
                    x *= -1
                    sharks[j][3] = 2
                elif x >= r:
                    x -= 2*(x-r+1)
                    sharks[j][3] = 1
                elif y < 0:
                    y *= -1
                    sharks[j][3] = 3
                elif y >= c:
                    y -= 2*(y-c+1)
                    sharks[j][3] = 4
                else:
                    break
            if tmp[x][y] == -1:
                tmp[x][y] = j
                sharks[j][0], sharks[j][1] = x, y
            else:
                if sharks[tmp[x][y]][4] > sharks[j][4]:
                    existence[j] = 0
                else:
                    existence[tmp[x][y]] = 0
                    tmp[x][y] = j
                    sharks[j][0], sharks[j][1] = x, y
    board = deepcopy(tmp)
print(ans)
def bfs(rx, ry, bx, by):
    visited = set()
    visited.add((rx, ry, bx, by))
    q = deque([(rx, ry, bx, by)])
    cnt = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if cnt > 10:
                return -1
            if board[rx][ry] == 'O':
                return cnt
            for i in range(4):
                nrx, nry = rx, ry
                while 1:
                    nrx += dx[i]
                    nry += dy[i]
                    if board[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if board[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while 1:
                    nbx += dx[i]
                    nby += dy[i]
                    if board[nbx][nby] == '#':
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if board[nbx][nby] == 'O':
                        break
                if board[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx + nry - ry) > abs(nbx - bx + nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited:
                    q.append((nrx, nry, nbx, nby))
                    visited.add((nrx, nry, nbx, nby))
        cnt += 1
    return -1

from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
board = [list(stdin.readline().rstrip()) for i in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            rx, ry = i, j
        if board[i][j] == 'B':
            bx, by = i, j
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
print(bfs(rx, ry, bx, by))
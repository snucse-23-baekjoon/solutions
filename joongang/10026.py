from sys import stdin
from collections import deque
n = int(stdin.readline())
lst = [stdin.readline().rstrip() for i in range(n)]
blind = 1
noblind = 1
visited_b = [[0 for i in range(n)] for j in range(n)]
visited_n = [[0 for i in range(n)] for j in range(n)]
queue_b = deque([(0, 0)])
queue_n = deque([(0, 0)])
visited_b[0][0] = 1
visited_n[0][0] = 1
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(n):
    for j in range(n):
        if not visited_b[i][j]:
            queue_b.append((i, j))
            visited_b[i][j] = 1
            blind += 1
        if not visited_n[i][j]:
            queue_n.append((i, j))
            visited_n[i][j] = 1
            noblind += 1
        while queue_b:
            a = queue_b[0][0]
            b = queue_b[0][1]
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if 0<=x<n and 0<=y<n and not visited_b[x][y] and (lst[a][b] == lst[x][y] or (lst[a][b] != 'B' and lst[x][y] != 'B')):
                    visited_b[x][y] = 1
                    queue_b.append((x, y))
            queue_b.popleft()
        while queue_n:
            a = queue_n[0][0]
            b = queue_n[0][1]
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if 0<=x<n and 0<=y<n and not visited_n[x][y] and lst[a][b] == lst[x][y]:
                    visited_n[x][y] = 1
                    queue_n.append((x, y))
            queue_n.popleft()
print(noblind, blind)
                
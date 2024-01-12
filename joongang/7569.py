from sys import stdin
from collections import deque
m, n, h = map(int, stdin.readline().split())
lst = []
queue = deque([])
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int, stdin.readline().split())))
        for k in range(m):
            if tmp[j][k] == 1:
                queue.append((i, j, k))
    lst.append(tmp)
dx = [1, 0, 0, -1, 0, 0]
dy = [0, 1, 0, 0, -1, 0]
dz = [0, 0, 1, 0, 0, -1]
while queue:
    a, b, c = queue.popleft()
    for i in range(6):
        x = a + dx[i]
        y = b + dy[i]
        z = c + dz[i]
        if 0<=x<h and 0<=y<n and 0<=z<m and lst[x][y][z] == 0:
            queue.append((x, y, z))
            lst[x][y][z] = lst[a][b][c] + 1
ans = 0
try:
    for i in lst:
        for j in i:
            for k in j:
                if k == 0:
                    raise
            ans = max(ans, max(j))
except:
    ans = 0
print(ans-1)
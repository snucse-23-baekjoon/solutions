def bfs(v):
    global lst, keys, document
    visited = [[0]*w for i in range(h)]
    visited[v[0]][v[1]] = 1
    q = deque([v])
    while q:
        a, b = q.popleft()
        for i in range(4):
            x = a + dx[i]
            y = b + dy[i]
            if 0<=x<h and 0<=y<w and not visited[x][y]:
                if ord('a')<=ord(lst[x][y])<=ord('z'):
                    if lst[x][y].upper() not in keys:
                        keys.add(lst[x][y].upper())
                        lst[x][y] = '.'
                        visited = [[0]*w for i in range(h)]
                        visited[x][y] = 1
                        q = deque([(x, y)])
                    else:
                        lst[x][y] = '.'
                        visited[x][y] = 1
                        q.append((x, y))
                elif lst[x][y] in ['.', '$'] or lst[x][y] in keys:
                    visited[x][y] = 1
                    q.append((x, y))
                    if lst[x][y] == '$':
                        document += 1
                        lst[x][y] = '.'

from sys import stdin
from collections import deque
t = int(stdin.readline())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for _ in range(t):
    h, w = map(int, stdin.readline().split())
    lst = []
    lst.append(['.']*(w+2))
    for i in range(h):
        lst.append(['.'] + list(stdin.readline().rstrip()) + ['.'])
    lst.append(['.']*(w+2))
    h += 2
    w += 2
    keys = stdin.readline().rstrip()
    if keys[0] == '0':
        keys = set()
    else:
        keys = set(keys.upper())
    document = 0
    bfs((0, 0))
    print(document)
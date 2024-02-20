from sys import stdin
from copy import deepcopy
lst = [list(stdin.readline().rstrip()) for i in range(10)]
for i in range(10):
    for j in range(10):
        if lst[i][j] == 'O':
            lst[i][j] = True
        else:
            lst[i][j] = False
dx = [-1, 1, 0, 0, 0]
dy = [0, 0, -1, 1, 0]
result = 101
for k in range(1024):
    tmp = deepcopy(lst)
    cnt = 0
    for i in range(10):
        if k&(1<<i):
            cnt += 1
            for j in range(1, 5):
                x = dx[j]
                y = i + dy[j]
                if 0<=y<10:
                    tmp[x][y] = not tmp[x][y]
    for i in range(1, 10):
        for j in range(10):
            if tmp[i-1][j]:
                cnt += 1
                for l in range(5):
                    x = i + dx[l]
                    y = j + dy[l]
                    if 0<=x<10 and 0<=y<10:
                        tmp[x][y] = not tmp[x][y]
    if not any(tmp[9]):
        result = min(result, cnt)
print(result if result != 101 else -1)
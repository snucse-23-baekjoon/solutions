import sys


n, m = map(int, sys.stdin.readline().split())
X = [[0] * (m + 2)]
for _ in range(n):
    X.append([0] + list(map(int, sys.stdin.readline().split())) + [0])
X.append([0] * (m + 2))
initial_loc = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if X[i][j] == 2:
            initial_loc = [i, j]
            X[i][j] = 0
        if X[i][j] == 1:
            X[i][j] = -1
to_search = [initial_loc]
d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
dist = 1
while to_search:
    tmp = []
    for loc in to_search:
        x, y = loc[0], loc[1]
        for dx, dy in d:
            if X[x + dx][y + dy] == -1:
                X[x + dx][y + dy] = dist
                tmp.append([x + dx, y + dy])
    to_search = tmp[:]
    dist += 1
for i in range(1, n + 1):
    print(*X[i][1: m + 1])

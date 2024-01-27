from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
s = [[0]*(n+1) for i in range(n+1)]
s[1][1] = lst[0][0]
for i in range(2, n+1):
    s[1][i] = s[1][i-1] + lst[0][i-1]
    s[i][1] = s[i-1][1] + lst[i-1][0]
for i in range(2, n+1):
    for j in range(2, n+1):
        s[i][j] = s[i-1][j] + s[i][j-1] + lst[i-1][j-1] - s[i-1][j-1]
for _ in range(m):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    print(s[x2][y2] - s[x2][y1-1] - s[x1-1][y2] + s[x1-1][y1-1])
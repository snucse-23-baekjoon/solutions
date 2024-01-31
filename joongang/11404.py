from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
d = [[float('inf')]*(n+1) for i in range(n+1)]
for _ in range(m):
    a, b, c = map(int, stdin.readline().split())
    d[a][b] = min(c, d[a][b])
for i in range(1, n+1):
    d[i][i] = 0
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            d[i][j] = min(d[i][j], d[i][k] + d[k][j])
for i in range(1, n+1):
    for j in range(1, n+1):
        if d[i][j] == float('inf'):
            d[i][j] = 0
        print(d[i][j], end=' ')
    print()
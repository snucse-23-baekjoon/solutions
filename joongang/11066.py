from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    lst = [0] + list(map(int, stdin.readline().split()))
    s = [0]
    for i in range(n):
        s.append(s[i]+lst[i+1])
    d = [[0]*(n+1) for i in range(n+1)]
    for i in range(2, n+1):
        for j in range(1, n+2-i):
            d[j][j+i-1] = min([d[j][j+k] + d[j+k+1][j+i-1] for k in range(i-1)]) + s[j+i-1] - s[j-1]
    print(d[1][n])
from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
inf = 2**31
d = [[inf]*n for i in range(n)]
for i in range(n):
    d[i][i] = 0
for i in range(n-1):
    for j in range(n-1-i):
        k = j+i+1
        for l in range(j, k):
            d[j][k] = min(d[j][k], d[j][l] + d[l+1][k] + lst[j][0]*lst[k][1]*lst[l][1])
print(d[0][-1])
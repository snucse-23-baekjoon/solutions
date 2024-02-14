def move(a, b):
    if a == 0:
        return 2
    if a == b:
        return 1
    if abs(a-b) == 2:
        return 4
    return 3

from sys import stdin
lst = list(map(int, stdin.readline().split()))
lst.pop()
n = len(lst)
if n == 0:
    print(0)
    exit(0)
d = [[[10**6]*5 for i in range(5)] for j in range(n+1)]
d[1][lst[0]][0] = 2
d[1][0][lst[0]] = 2
for i in range(1, n):
    target = lst[i]
    for j in range(5):
        for k in range(5):
            d[i+1][j][target] = min(d[i+1][j][target], d[i][j][k]+move(k, target))
            d[i+1][target][k] = min(d[i+1][target][k], d[i][j][k]+move(j, target))
M = 10**9
for i in range(5):
    for j in range(5):
        if i != j and d[n][i][j]:
            M = min(M, d[n][i][j])
print(M)
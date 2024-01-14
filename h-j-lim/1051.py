import sys


N, M = map(int, input().split())
mat = []
for i in range(N):
    row = list(sys.stdin.readline().rstrip())
    mat.append(row)
a = N + 1 if N <= M else M + 1
flag = 1
while flag:
    a -= 1
    for i in range(N - a + 1):
        for j in range(M - a + 1):
            if mat[i][j] == mat[i + a - 1][j] == mat[i][j + a - 1] == mat[i + a - 1][j + a - 1]:
                flag = 0
print(a ** 2)

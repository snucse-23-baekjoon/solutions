import sys


N, M = map(int, sys.stdin.readline().split())
X = []
for _ in range(N):
    X.append(list(map(int, sys.stdin.readline().split())))
A = []
for i in range(N):
    tmp = 0
    cumulative_sum = []
    for j in range(N):
        tmp += X[i][j]
        if i == 0:
            cumulative_sum.append(tmp)
        else:
            cumulative_sum.append(tmp + A[i - 1][j])
    A.append(cumulative_sum)
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    if x1 == 1 and y1 == 1:
        print(A[x2 - 1][y2 - 1])
    elif x1 == 1:
        print(A[x2 - 1][y2 - 1] - A[x2 - 1][y1 - 2])
    elif y1 == 1:
        print(A[x2 - 1][y2 - 1] - A[x1 - 2][y2 - 1])
    else:
        print(A[x2 - 1][y2 - 1] - A[x2 - 1][y1 - 2] - A[x1 - 2][y2 - 1] + A[x1 - 2][y1 - 2])


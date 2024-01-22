import sys


N, M = map(int, input().split())
L = []
for _ in range(N):
    L.append(list(sys.stdin.readline().rstrip()))


def func(r, c):
    return ((r + 1) * (2 * N - r)) * ((c + 1) * (2 * M - c))


D = {}
for i in range(N):
    for j in range(M):
        if L[i][j] not in D:
            D[L[i][j]] = func(i, j) + func(i + N, j) + func(i, j + M) + func(i + N, j + M)
        else:
            D[L[i][j]] += func(i, j) + func(i + N, j) + func(i, j + M) + func(i + N, j + M)

for i in range(ord('A'), ord('Z') + 1):
    if chr(i) in D:
        print(D[chr(i)])
    else:
        print(0)

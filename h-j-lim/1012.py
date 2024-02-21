import sys


def adjacent(r, c):
    lettuce[r][c] = 0
    if r > 0 and lettuce[r - 1][c] == 1:
        adjacent(r - 1, c)
    if c < M - 1 and lettuce[r][c + 1] == 1:
        adjacent(r, c + 1)
    if r < N - 1 and lettuce[r + 1][c] == 1:
        adjacent(r + 1, c)
    if c > 0 and lettuce[r][c - 1] == 1:
        adjacent(r, c - 1)


sys.setrecursionlimit(10 ** 5)
T = int(sys.stdin.readline())
for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    lettuce = [[0] * M for _ in range(N)]
    for _ in range(K):
        m, n = map(int, sys.stdin.readline().split())
        lettuce[n][m] = 1
    ans = 0
    for i in range(N):
        for j in range(M):
            if lettuce[i][j] == 1:
                ans += 1
                adjacent(i, j)
    print(ans)

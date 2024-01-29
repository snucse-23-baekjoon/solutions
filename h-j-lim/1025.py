import sys


N, M = map(int, sys.stdin.readline().split())
Mat = []
for _ in range(N):
    Mat.append(list(map(int, list(sys.stdin.readline().rstrip()))))
ans = -1
for i in range(N):
    for j in range(M):  # start position: i, j
        vertical_range = list(range(-i, N + 1 - i))
        horizontal_range = list(range(-j, M + 1 - j))
        for k in vertical_range:
            for l in horizontal_range:
                m = 0
                num = 0
                if not (k == 0 and l == 0):
                    while 0 <= i + k * m < N and 0 <= j + l * m < M:
                        num = 10 * num + Mat[i + k * m][j + l * m]
                        if (num ** 0.5) % 1 == 0 and num > ans:
                            ans = num
                        m += 1
print(ans)

import sys
sys.stdin = open("../input.txt", 'r')

M = 10_007
N = int(sys.stdin.readline())

binom = [[0] * 53 for _ in range(53)]
for n in range(53):
    for r in range(n + 1):
        if r == 0 or r == n:
            binom[n][r] = 1
        else:
            binom[n][r] = binom[n - 1][r - 1] + binom[n - 1][r]
            binom[n][r] %= M

i = 1
result = 0
while N - 4 * i >= 0:
    result += binom[13][i] * binom[52 - 4 * i][N - 4 * i] * (2 * (i % 2) - 1)
    result %= M
    i += 1

print(result)

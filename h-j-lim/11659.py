import sys


N, M = map(int, sys.stdin.readline().split())
L = list(map(int, sys.stdin.readline().split()))
L_cumulative_sum = []
tmp = 0
for i in range(N):
    tmp += L[i]
    L_cumulative_sum.append(tmp)
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(L_cumulative_sum[b - 1] - L_cumulative_sum[a - 1] + L[a - 1])

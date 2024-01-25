import sys


N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
DP = L[0]
i = 1
while i < N:
    tmp = DP[:]
    DP[0] = min(tmp[1] + L[i][0], tmp[2] + L[i][0])
    DP[1] = min(tmp[0] + L[i][1], tmp[2] + L[i][1])
    DP[2] = min(tmp[0] + L[i][2], tmp[1] + L[i][2])
    i += 1
print(min(DP))

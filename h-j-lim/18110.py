import sys


N = int(sys.stdin.readline())
L = []
for _ in range(N):
    L.append(int(sys.stdin.readline()))
if N == 0:
    ans = 0
elif N <= 3:
    ans = sum(L) / N
else:
    L.sort()
    p_15 = int((N * 0.15) + 0.5)
    ans = sum(L[p_15: -p_15]) / (N - 2 * p_15)
print(int(ans + 0.5))

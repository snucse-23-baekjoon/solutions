import sys
import functools


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
L1, L2 = [], []
for i in range(N):
    L1.append(int(sys.stdin.readline()))
for i in range(N - 1):
    L2.append(L1[i + 1] - L1[i])
gcd_L2 = functools.reduce(gcd, L2)
print(sum(map(lambda x: x // gcd_L2 - 1, L2)))

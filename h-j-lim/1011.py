import sys


def sol(d):
    n = int(d ** (1 / 2))
    if d == n ** 2:
        return 2 * n - 1
    else:
        if d - n ** 2 <= n:
            return 2 * n
        else:
            return 2 * n + 1


T = int(sys.stdin.readline())
for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    dist = y - x
    print(sol(dist))

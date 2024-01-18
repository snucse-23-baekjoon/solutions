import sys


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)


def combination(x, y):  # x C y
    return fact(x) // (fact(y) * fact(x - y))


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    print(combination(M, N))

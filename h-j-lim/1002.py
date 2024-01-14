import sys


memo = [(1, 0), (0, 1)] + [(0, 0)] * 39


def fibonacci(n):
    if memo[n] != (0, 0):
        return memo[n]
    else:
        memo[n] = tuple(map(lambda a, b: a + b, fibonacci(n - 1), fibonacci(n - 2)))
        return memo[n]


T = int(input())
for i in range(T):
    N = int(sys.stdin.readline())
    print(*fibonacci(N))

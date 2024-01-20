import sys


memo = [0, 1, 1, 1, 2, 2] + [0] * 95


def func1(n):
    if memo[n] == 0:
        memo[n] = func1(n - 1) + func1(n - 5)
    return memo[n]


T = int(input())
for _ in range(T):
    x = int(sys.stdin.readline())
    print(func1(x))

memo = [0, 1, 1] + [0] * 88


def func(n):
    if memo[n]:
        return memo[n]
    else:
        memo[n] = sum(map(lambda x: func(x), range(1, n - 1))) + 1
        return memo[n]


N = int(input())
print(func(N))

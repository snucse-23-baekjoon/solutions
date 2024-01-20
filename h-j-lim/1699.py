L = [0] * 100001


def func(n):
    if L[n]:
        return L[n]
    if n ** (1/2) % 1 == 0:
        L[n] = 1
        return L[n]
    L[n] = min(map(lambda x: func(n - x ** 2), range(int(n ** (1/2)), 0, -1))) + 1
    return L[n]


N = int(input())
print(func(N))

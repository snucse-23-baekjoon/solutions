L = [1] + [0] * 10


def fact(n):
    if L[n]:
        return L[n]
    L[n] = n * fact(n - 1)
    return L[n]


N, K = map(int, input().split())
print(fact(N) // (fact(K) * fact(N - K)))

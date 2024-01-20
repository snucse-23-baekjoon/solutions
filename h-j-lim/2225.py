def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


N, K = map(int, input().split())

print((fact(K + N - 1) // (fact(N) * fact(K - 1))) % 1000000000)

D = {}
for i in range(1, 1001):
    D[(i, 0)], D[(i, i)] = 1, 1
    D[(i, 1)], D[(i, i - 1)] = i, i


def combination(n, k):
    if (n, k) in D.keys():
        return D[(n, k)]
    elif (n, n - k) in D.keys():
        return D[(n, n - k)]
    else:
        D[(n, k)] = combination(n - 1, k) + combination(n - 1, k - 1)
        D[(n, n - k)] = D[(n, k)]
        return D[(n, k)]


N, K = map(int, input().split())
print(combination(N, K) % 10007)

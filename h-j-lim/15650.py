def n_and_m(n, m, permutation, last, length):
    if length == m:
        ans.append(permutation)
    else:
        if n - last >= m - length:
            for num in range(last + 1, n + 1):
                n_and_m(n, m, permutation + [num], num, length + 1)


N, M = map(int, input().split())
ans = []
n_and_m(N, M, [], 0, 0)
for p in ans:
    print(*p)

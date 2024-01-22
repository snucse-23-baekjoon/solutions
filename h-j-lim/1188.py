N, M = map(int, input().split())
s, n, c = 0, 0, 0
if N % M == 0:
    print(0)
else:
    if N > M:
        N = N - M * (N // M)
    while s < N * M:
        s += N % M
        new_n = s // M
        if new_n == n:
            c += 1
        elif s % M == 0:
            c = c
        else:
            c += 1
        n = new_n
    print(c)

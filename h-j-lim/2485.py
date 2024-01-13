M, N = map(int, input().split())
L = list(range(N + 1))
for i in range(2, N + 1):
    if L[i] >= M:
        print(L[i])
    L[i::i] = (N // i) * [0]

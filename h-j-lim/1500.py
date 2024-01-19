S, K = map(int, input().split())
N = [S // K] * K
N[:S % K] = list(map(lambda x: x + 1, N[:S % K]))
A = 1
for num in N:
    A *= num
print(A)

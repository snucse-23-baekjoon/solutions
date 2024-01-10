N, K = map(int, input().split())
C, A = 1, 1
while C < K and A <= N:
    A = A + 1
    if N % A == 0:
        C += 1
if C < K:
    print(0)
else:
    print(A)

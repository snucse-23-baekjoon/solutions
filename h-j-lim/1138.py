N, S = map(int, input().split())
L = list(map(int, input().split()))
A = [0]
for i in L:
    B = A[:]
    for j in B:
        A += [i + j]
print(A[1:].count(S))

A = []
C = []
N, M = map(int, input().split())
for i in range(N):
    A.append(list(map(int, input().split())))
for i in range(N):
    row_to_add = list(map(int, input().split()))
    C.append(list(map(lambda a, b: a + b, A[i], row_to_add)))
for row in C:
    print(' '.join(map(str, row)))

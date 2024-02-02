import sys


N = int(input())
L = []
for _ in range(N):
    X = sys.stdin.readline().rstrip()
    if X not in L:
        L.append(X)
L.sort(key=lambda x: len(x))
i = 0
while i < len(L):
    j = 1
    while i + j < len(L) and len(L[i]) == len(L[i + j]):
        j += 1
    L[i: i + j] = sorted(L[i: i + j])
    i += j
for y in L:
    print(y)

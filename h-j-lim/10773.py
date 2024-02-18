import sys


K = int(sys.stdin.readline())
L = []
for _ in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        L.pop()
    else:
        L.append(N)
if len(L) == 0:
    print(0)
else:
    print(sum(L))

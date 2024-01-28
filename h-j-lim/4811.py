import sys


D = {0: 1, 1: 1}
N = int(sys.stdin.readline())
while N:
    if N not in D.keys():
        for i in range(max(D.keys()) + 1, N + 1):
            D[i] = sum(map(lambda x: D[x] * D[i - 1 - x], range(i)))
    print(D[N])
    N = int(sys.stdin.readline())

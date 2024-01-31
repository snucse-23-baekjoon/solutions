import sys


T = int(sys.stdin.readline())
for _ in range(T):
    D = {}
    N = int(sys.stdin.readline())
    for _ in range(N):
        a, b = map(int, sys.stdin.readline().split())
        D[a] = b
    c = 1
    tmp = D[1]
    for i in range(2, N + 1):
        if D[i] < tmp:
            c += 1
            tmp = D[i]
    print(c)

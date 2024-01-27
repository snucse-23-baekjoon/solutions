import sys


D = {0: 1, 1: 1}
T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    if L % 2:
        print(0)
    else:
        if L // 2 in D.keys():
            print(D[L // 2] % 1000000007)
        else:
            n = L // 2
            for i in range(max(D.keys()), n):
                D[i + 1] = sum(map(lambda x: D[x] * D[i - x], range(i + 1)))
            print(D[n] % 1000000007)

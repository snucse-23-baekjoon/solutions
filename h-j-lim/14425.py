import sys


N, M = map(int, input().split())
D1, D2 = {}, {}
L = []
for i in range(N):
    x = sys.stdin.readline().rstrip()
    D1[i + 1] = x
    D2[x] = i + 1
for i in range(M):
    L.append(sys.stdin.readline().rstrip())
for a in L:
    if a.isdigit():
        print(D1[int(a)])
    else:
        print(D2[a])

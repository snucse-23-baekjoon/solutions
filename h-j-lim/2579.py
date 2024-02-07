import sys


N = int(sys.stdin.readline())
stairs = [0]
for _ in range(N):
    stairs.append(int(sys.stdin.readline()))
L = [[0, 0], [stairs[1], stairs[1]]] + [[0, 0]] * (N - 1)
for i in range(2, N + 1):
    L[i] = [L[i - 1][1] + stairs[i], max(L[i - 2]) + stairs[i]]
print(max(L[N]))

import sys


T = int(sys.stdin.readline())
L = [[0, 0, 0], [0, 1, 0]]
for i in range(2, 12):
    prev = L[i - 1]
    L.append([prev[1] + 2 * prev[2], prev[0], prev[1] + prev[2]])
L1 = list(map(sum, L))
for _ in range(T):
    n = int(sys.stdin.readline())
    print(L1[n])

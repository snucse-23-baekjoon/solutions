import sys


N = int(input())
L1 = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    L1.append(A - B)
L1.sort()
h = len(L1) // 2
if len(L1) % 2 == 1:
    if L1[h] % 1 == 0:
        print(1)
    else:
        print(2)
else:
    if L1[h] % 1 == 0 and L1[h - 1] % 1 == 0:
        print(int(L1[h] - L1[h - 1] + 1))
    else:
        print(int(L1[h]) - int(L1[h - 1]))

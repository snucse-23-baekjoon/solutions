import sys


N = int(sys.stdin.readline())
L = []
for _ in range(N):
    a, b = map(int, sys.stdin.readline().split())
    L.append((a, b))
L.sort(key=lambda x: x[0])
L.sort(key=lambda x: x[1])
c = 0
tmp = (-1, -1)
for meeting in L:
    if meeting[0] >= tmp[1]:
        tmp = meeting
        c += 1
print(c)

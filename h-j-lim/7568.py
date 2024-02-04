import sys


N = int(sys.stdin.readline())
L = []
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
ans = []
for i in range(N):
    c = 1
    for j in range(N):
        if L[i][0] < L[j][0] and L[i][1] < L[j][1]:
            c += 1
    ans.append(c)
print(*ans)

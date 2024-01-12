import sys


N, M = map(int, input().split())
S = set()
count = 0
for i in range(N + M):
    x = sys.stdin.readline()
    if i < N:
        S.add(x)
    else:
        if x in S:
            count += 1
print(count)

import sys


N = int(input())
S = set()
S.add('ChongChong')
count = 1
for i in range(N):
    x = sys.stdin.readline().split()
    if x[0] in S or x[1] in S:
        S.add(x[0])
        S.add(x[1])
print(len(S))

import sys


N = int(input())
S = set()
count = 0
for i in range(N):
    x = sys.stdin.readline().rstrip()
    if x == 'ENTER':
        count += len(S)
        S.clear()
    else:
        S.add(x)
count += len(S)
print(count)

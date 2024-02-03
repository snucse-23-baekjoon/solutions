import sys


K, N = map(int, sys.stdin.readline().split())
L = []
for _ in range(K):
    L.append(int(sys.stdin.readline()))
left = 0
right = max(L)
while left + 1 < right:
    mid = (left + right) // 2
    x = sum(map(lambda y: y // mid, L))
    if x >= N:
        left = mid
    else:
        right = mid
if sum(map(lambda y: y // right, L)) >= N:
    print(right)
else:
    print(left)

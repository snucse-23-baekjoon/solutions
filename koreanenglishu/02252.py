import sys
from collections import deque
sys.stdin = open("../input.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
in_deg = [0 for _ in range(N)]

for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    A, B = A - 1, B - 1
    adj_list[A].append(B)
    in_deg[B] += 1

queue = deque([])
for u in range(N):
    if in_deg[u] == 0:
        queue.append(u)

while queue:
    u = queue.popleft()
    print(u + 1, end=' ')
    for v in adj_list[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)
print()

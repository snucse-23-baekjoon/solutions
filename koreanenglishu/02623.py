import sys
from collections import deque
sys.stdin = open("../input.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
adj_list = [[] for _ in range(N)]
in_deg = [0 for _ in range(N)]

for _ in range(M):
    porder = list(map(int, sys.stdin.readline().split()))
    for i in range(1, len(porder) - 1):
        u, v = porder[i], porder[i + 1]
        u, v = u - 1, v - 1
        adj_list[u].append(v)
        in_deg[v] += 1

queue = deque([])
for u in range(N):
    if in_deg[u] == 0:
        queue.append(u)

order = []
visit = [False for _ in range(N)]
while queue:
    u = queue.popleft()
    order.append(str(u + 1))
    visit[u] = True
    for v in adj_list[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)

if all(visit):
    print('\n'.join(order))
else:
    print("0")

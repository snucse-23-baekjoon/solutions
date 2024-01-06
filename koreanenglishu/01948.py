import sys
from collections import deque
sys.stdin = open("../input.txt", 'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
adj_list = [[] for _ in range(N)]
back_adj_list = [[] for _ in range(N)]
in_deg = [0 for _ in range(N)]
time_count = [0 for _ in range(N)]
edge_count = [0 for _ in range(N)]
visited = [False for _ in range(N)]

for _ in range(M):
    u, v, t = map(int, sys.stdin.readline().split())
    u, v = u - 1, v - 1
    adj_list[u].append((v, t))
    back_adj_list[v].append((u, t))
    in_deg[v] += 1

S, E = map(int, sys.stdin.readline().split())
S, E = S - 1, E - 1

queue = deque([S])
while queue:
    u = queue.popleft()
    for v, t in adj_list[u]:
        in_deg[v] -= 1
        if in_deg[v] == 0:
            queue.append(v)
        if time_count[v] < time_count[u] + t:
            time_count[v] = time_count[u] + t

edge_count = 0
queue = deque([E])
while queue:
    u = queue.popleft()
    for v, t in back_adj_list[u]:
        if time_count[u] == time_count[v] + t:
            edge_count += 1
            if not visited[v]:
                queue.append(v)
                visited[v] = True

print(time_count[E])
print(edge_count)

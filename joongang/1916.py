def dijkstra(s, e):
    d = {i: float('inf') for i in range(1, n+1)}
    d[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, cur = heapq.heappop(q)
        if dist > d[cur]:
            continue
        for i, j in E[cur]:
            cost = dist + j
            if cost < d[i]:
                d[i] = cost
                heapq.heappush(q, (cost, i))
    return d[e]

from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
E = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    E[x].append((y, z))
s, e = map(int, stdin.readline().split())
print(dijkstra(s, e))
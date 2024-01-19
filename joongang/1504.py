def dijkstra(v):
    d = [float('inf')] * (n+1)
    q = []
    heapq.heappush(q, (0, v))
    d[v] = 0
    while q:
        dist, cur = heapq.heappop(q)
        if d[cur] < dist:
            continue
        for i in E[cur]:
            cost = d[cur] + E[cur][i]
            if d[i] > cost:
                d[i] = cost
                heapq.heappush(q, (cost, i))
    return d
        
from sys import stdin
import heapq
n, e = map(int, stdin.readline().split())
E = {i: dict() for i in range(1, n+1)}
for _ in range(e):
    a, b, c = map(int, stdin.readline().split())
    E[a][b] = c
    E[b][a] = c
v1, v2 = map(int, stdin.readline().split())
d1 = dijkstra(1)
d2 = dijkstra(v1)
d3 = dijkstra(v2)
r1 = d1[v1]+d2[v2]+d3[n]
r2 = d1[v2]+d3[v1]+d2[n]
if (r1 == float('inf')) and (r2 == float('inf')):
    print(-1)
else:
    print(min(r1, r2))
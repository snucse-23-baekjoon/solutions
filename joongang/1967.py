def dijkstra(v):
    d = [0] + [float('inf') for i in range(n)]
    d[v] = 0
    q = []
    heapq.heappush(q, (0, v))
    while q:
        dist, cur = heapq.heappop(q)
        if dist > d[cur]:
            continue
        for i in E[cur]:
            cost = dist + E[cur][i]
            if cost < d[i]:
                d[i] = cost
                heapq.heappush(q, (cost, i))
    return d

from sys import stdin
import heapq
n = int(stdin.readline())
E = {i: dict() for i in range(1, n+1)}
for _ in range(n-1):
    x, y, z = map(int, stdin.readline().split())
    E[x][y] = z
    E[y][x] = z
if n == 1:
    print(0)
    exit(0)
d1 = dijkstra(1)
v = d1.index(max(d1))
print(max(dijkstra(v)))
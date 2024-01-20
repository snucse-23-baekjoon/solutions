def dijkstra(k):
    d = {i: float('inf') for i in range(1, v+1)}
    d[k] = 0
    q = []
    heapq.heappush(q, (d[k], k))
    while q:
        dist, cur = heapq.heappop(q)
        if dist > d[cur]:
            continue
        for i, j in graph[cur]:
            cost = dist + j
            if cost < d[i]:
                d[i] = cost
                heapq.heappush(q, (cost, i))
    return d

from sys import stdin
import heapq
v, e = map(int, stdin.readline().split())
k = int(stdin.readline())
graph = {i: [] for i in range(1, v+1)}
for _ in range(e):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append((y, z))
d = dijkstra(k)
for i in range(1, v+1):
    if d[i] == float('inf'):
        print('INF')
    else:
        print(d[i])
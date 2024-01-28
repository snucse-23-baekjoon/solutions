def dijkstra(s, e, graph):
    d = {i: float('inf') for i in range(1, n+1)}
    route = {i: [s] for i in range(1, n+1)}
    d[s] = 0
    q = []
    heapq.heappush(q, (0, s))
    while q:
        dist, cur = heapq.heappop(q)
        if d[cur] < dist:
            continue
        for i, j in graph[cur]:
            cost = dist + j
            if d[i] > cost:
                d[i] = cost
                heapq.heappush(q, (cost, i))
                route[i] = route[cur] + [i]
    return d[e], route[e]

from sys import stdin
import heapq
n = int(stdin.readline())
m = int(stdin.readline())
graph = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    graph[x].append((y, z))
s, e = map(int, stdin.readline().split())
d, route = dijkstra(s, e, graph)
print(d)
print(len(route))
print(' '.join(map(str, route)))
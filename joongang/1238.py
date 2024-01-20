def dijkstra(E, d):
    d[x-1] = 0
    heap = []
    heapq.heappush(heap, (0, x))
    while heap:
        dist, cur = heapq.heappop(heap)
        if d[cur-1] < dist:
            continue
        for i in E[cur]:
            if d[i-1] > d[cur-1] + E[cur][i]:
                d[i-1] = d[cur-1] + E[cur][i]
                heapq.heappush(heap, (d[i-1], i))
    return d
        
from sys import stdin
import heapq
n, m, x = map(int, stdin.readline().split())
E1 = {i: dict() for i in range(1, n+1)}
E2 = {i: dict() for i in range(1, n+1)}
for _ in range(m):
    start, end, t = map(int, stdin.readline().split())
    E1[end][start] = t
    E2[start][end] = t
d1 = [1000000]*n
d2 = [1000000]*n
d1 = dijkstra(E1, d1)
d2 = dijkstra(E2, d2)
d = []
for i in range(n):
    d.append(d1[i]+d2[i])
print(max(d))
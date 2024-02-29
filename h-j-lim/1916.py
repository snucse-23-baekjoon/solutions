import sys


N = int(input())
M = int(input())
max_tmp = 0
G = [[[i, 0]] for i in range(N)]
for _ in range(M):
    x1, x2, x3 = map(int, sys.stdin.readline().split())
    G[x1 - 1].append([x2 - 1, x3])
    max_tmp += x3
origin, destination = map(int, sys.stdin.readline().split())
origin -= 1
destination -= 1
unvisited = set(range(N))
d = [max_tmp + 1] * N
d[origin] = 0
node = origin
route = [[i] for i in range(N)]
while destination in unvisited:
    for edge in G[node]:
        dist = d[node] + edge[1]
        if dist < d[edge[0]]:
            d[edge[0]] = dist
            route[edge[0]] = route[node] + [edge[0]]
    unvisited.remove(node)
    if unvisited:
        node = min(unvisited, key=lambda x: d[x])
print(d[destination])
print(len(route[destination]))
print(*list(map(lambda x: x + 1, route[destination])))


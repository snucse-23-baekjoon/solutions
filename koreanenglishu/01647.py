import sys
sys.setrecursionlimit(1_000_000)
sys.stdin = open("../input.txt", 'r')

def find(parents, x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]

def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x < y:
        parents[x] = y
    else:
        parents[y] = x

V, E = map(int, sys.stdin.readline().split())
parents = [i for i in range(V)]

edges = []
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().split())
    u, v, w = A - 1, B - 1, C
    edges.append((u, v, w))
edges.sort(key=lambda x: x[2])

w_sum = 0
w_max = 0
for u, v, w in edges:
    find(parents, u)
    find(parents, v)
    if parents[u] != parents[v]:
        union(parents, u, v)
        w_sum += w
        w_max = w

w_sum -= w_max
print(w_sum)

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

N, M = map(int, sys.stdin.readline().split())
parents = [i for i in range(N)]

result = 0
for i in range(1, M + 1):
    u, v = map(int, sys.stdin.readline().split())
    find(parents, u)
    find(parents, v)
    if parents[u] == parents[v]:
        result = i
        break
    else:
        union(parents, u, v)

print(result)

def f(v):
    print(v, end=' ')
    indegree[v] -= 1
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            f(i)

import sys
from sys import stdin
sys.setrecursionlimit(10**9)
n, m = map(int, stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}
indegree = {i: 0 for i in range(1, n+1)}
for i in range(m):
    a, b = map(int, stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1
for i in range(1, n+1):
    if indegree[i] == 0:
        f(i)
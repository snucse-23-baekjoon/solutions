def tsort(v):
    order.append(v)
    for i in graph[v]:
        indegree[i] -= 1
        if indegree[i] == 0:
            indegree[i] -= 1
            tsort(i)

from sys import stdin
n, m = map(int, stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}
indegree = {i: 0 for i in range(1, n+1)}
for i in range(m):
    lst = list(map(int, stdin.readline().split()))
    for j in range(1, lst[0]):
        graph[lst[j]].append(lst[j+1])
        indegree[lst[j+1]] += 1
order = []
for i in graph:
    if indegree[i] == 0:
        indegree[i] -= 1
        tsort(i)
if len(order) != n:
    print(0)
else:
    for i in order:
        print(i)
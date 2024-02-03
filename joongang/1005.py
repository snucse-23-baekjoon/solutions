from sys import stdin
from collections import deque
t = int(stdin.readline())
for _ in range(t):
    n, k = map(int, stdin.readline().split())
    times = [0] + list(map(int, stdin.readline().split()))
    graph = {i: [] for i in range(1, n+1)}
    indegree = {i: 0 for i in range(1, n+1)}
    d = {i: 0 for i in range(1, n+1)}
    for __ in range(k):
        x, y = map(int, stdin.readline().split())
        graph[x].append(y)
        indegree[y] += 1
    w = int(stdin.readline())
    q = deque([])
    for i in graph:
        if not indegree[i]:
            q.append(i)
            d[i] = times[i]
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            indegree[i] -= 1
            d[i] = max(d[i], d[cur]+times[i])
            if indegree[i] == 0:
                q.append(i)
    print(d[w])
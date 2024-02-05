from sys import stdin
n, m = map(int, stdin.readline().split())
graph = {i: [] for i in range(1, n+1)}
indegree = {i: 0 for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    graph[x].append(y)
    indegree[y] += 1
chk = 0
while chk < n:
    for i in range(1, n+1):
        if indegree[i] == 0:
            print(i, end=' ')
            indegree[i] -= 1
            for j in graph[i]:
                indegree[j] -= 1
            chk += 1
            break
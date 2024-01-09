def bfs(E, v, t):
    visited = {i: 0 for i in range(1, len(E)+1)}
    visited[v] = 1
    queue = [v]
    dist = 0
    level = v
    while queue[0] != t:
        for i in E[queue[0]]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1
        if queue[0] == level:
            level = queue[-1]
            dist += 1
        queue.pop(0)
    return dist
    
from sys import stdin
n, m = map(int, stdin.readline().split())
E = {i: [] for i in range(1, n+1)}
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    E[x].append(y)
    E[y].append(x)
score = [0 for i in range(n)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if i != j:
            score[i-1] += bfs(E, i, j)
print(score.index(min(score))+1)
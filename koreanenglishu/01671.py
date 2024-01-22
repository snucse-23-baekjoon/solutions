from sys import stdin
stdin = open("../input.txt", 'r')

def dfs(u):
    if visited[u]: return 0
    visited[u] = 1
    for v in graph[u]:
        w = selected[v]
        if w == -1 or dfs(w):
            selected[v] = u; return 1
    return 0

sharks = []
n = int(stdin.readline())
graph = [[] for _ in range(2 * n)]
for i in range(n):
    a1, b1, c1 = map(int, stdin.readline().split())
    for j in range(i):
        a2, b2, c2 = sharks[j]
        if a1 >= a2 and b1 >= b2 and c1 >= c2:
            graph[i].append(j); graph[n + i].append(j)
        elif a1 <= a2 and b1 <= b2 and c1 <= c2:
            graph[j].append(i); graph[n + j].append(i)
    sharks.append((a1, b1, c1))

die = 0
selected = [-1] * n
for i in range(2 * n):
    visited = [0] * (2 * n)
    die += dfs(i)
print(n - die)

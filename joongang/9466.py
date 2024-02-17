def dfs(v):
    global cnt
    visited[v] = 1
    cycle.append(v)
    if visited[choice[v]]:
        if choice[v] in cycle:
            cnt += len(cycle[cycle.index(choice[v]):])
    else:
        dfs(choice[v])

import sys
from sys import stdin
sys.setrecursionlimit(10**6)
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    choice = [0] + list(map(int, stdin.readline().split()))
    visited = [0]*(n+1)
    cnt = 0
    for i in range(1, n+1):
        if not visited[i]:
            cycle = []
            dfs(i)
    print(n - cnt)
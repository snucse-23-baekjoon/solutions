def dfs(cur, visited):
    if visited == (1<<n)-1:
        if matrix[cur][0]:
            return matrix[cur][0]
        else:
            return float('inf')
    if (cur, visited) in dp:
        return dp[(cur, visited)]
    m = float('inf')
    for i in range(1, n):
        if matrix[cur][i] == 0 or (visited & (1<<i)):
            continue
        cost = dfs(i, visited|(1<<i)) + matrix[cur][i]
        m = min(m, cost)
    dp[(cur, visited)] = m
    return m

from sys import stdin
n = int(stdin.readline())
matrix = [list(map(int, stdin.readline().split())) for i in range(n)]
dp = {}
print(dfs(0, 1))
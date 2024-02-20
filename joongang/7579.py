from sys import stdin
n, m = map(int, stdin.readline().split())
memoryuse = [0] + list(map(int, stdin.readline().split()))
additionalcost = [0] + list(map(int, stdin.readline().split()))
s = sum(additionalcost)
d = [[0]*(s+1) for i in range(n+1)]
result = 10**7
for i in range(1, n+1):
    mem = memoryuse[i]
    cost = additionalcost[i]
    for j in range(s+1):
        if j < additionalcost[i]:
            d[i][j] = d[i-1][j]
        else:
            d[i][j] = max(d[i-1][j], d[i-1][j-cost] + mem)
        if d[i][j] >= m:
            result = min(result, j)
print(result)
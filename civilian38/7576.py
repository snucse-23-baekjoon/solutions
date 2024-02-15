import sys

m, n = map(int, sys.stdin.readline().split())
graph = list()
pre = set()

for i in range(n):
    line = tuple(map(int, sys.stdin.readline().split()))
    graph.append([])
    for j in range(m):
        if line[j] == 1:
            pre.add((i, j))
        graph[-1].append(line[j])

count = 0

while pre:
    post = set()
    for x, y in pre:
        graph[x][y] = 1
        for i, j in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if 0 <= x + i < n and 0 <= y + j < m:
                if graph[x + i][y + j] == 0 and (x + i, y + j) not in pre:
                    post.add((x + i, y + j))
    pre = post
    count += 1
    
if any(filter(lambda x: 0 in x, graph)):
    print(-1)
else:
    print(count - 1)
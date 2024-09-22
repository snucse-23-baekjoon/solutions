import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
graph = dict()
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    if graph.get(a):
        graph[a].add(b)
    else:
        graph[a] = set([b])
    if graph.get(b):
        graph[b].add(a)
    else:
        graph[b] = set([a])

element = [i for i in range(1, 1 + n)]
count = 0
index = 0
while any(filter(lambda x: x > 0, element)):
    while not element[index]:
        index += 1
    node = element[index]
    neighbors = deque([node])
    while neighbors:
        target = neighbors.popleft()
        if element[target - 1]:
            element[target - 1] = 0
            if graph.get(target):
                for item in graph[target]:
                    neighbors.append(item)
    count += 1
    
print(count)
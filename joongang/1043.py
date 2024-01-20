def bfs(E, v):
    global d
    queue = deque([v])
    while queue:
        for i in E[queue[0]]:
            if not d[i]:
                queue.append(i)
                d[i] = 1
        queue.popleft()
        
from sys import stdin
from collections import deque
n, m = map(int, stdin.readline().split())
know = stdin.readline().rstrip().split()
if len(know) > 1:
    knowlst = list(map(int, know[1:]))
else:
    knowlst = []
d = {i: 1 if i in knowlst else 0 for i in range(1, n+1)}
party = [list(map(int, stdin.readline().split()[1:])) for i in range(m)]
E = {i: set() for i in range(1, n+1)}
for i in party:
    for j in range(len(i)):
        for k in range(len(i)):
            if j != k:
                E[i[j]].add(i[k])
                E[i[k]].add(i[j])
for i in knowlst[:]:
    bfs(E, i)
ans = 0
for i in party:
    chk = 0
    for j in i:
        if d[j]:
            chk = 1
            break
    if not chk:
        ans += 1
print(ans)
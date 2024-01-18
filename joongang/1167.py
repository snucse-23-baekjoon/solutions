def dfs(v, E, root):
    global distlst
    visited = {i: 0 for i in range(1, v+1)}
    def search(cur, dist):
        visited[cur] = 1
        chk = 0
        for i in E[cur]:
            if not visited[i[0]]:
                search(i[0], dist + i[1])
                chk = 1
        if not chk:
            distlst.append((dist, cur))
    search(root, 0)

from sys import stdin
v = int(stdin.readline())
E = {i: [] for i in range(1, v+1)}
for _ in range(v):
    node = list(map(int, stdin.readline().split()))
    for i in range(1, len(node)-1, 2):
        E[node[0]].append((node[i], node[i+1]))
root = 1
distlst = []
dfs(v, E, root)
distlst.sort(key = lambda x: x[0])
root = distlst[-1][1]
distlst = []
dfs(v, E, root)
distlst.sort(key = lambda x: x[0])
print(distlst[-1][0])
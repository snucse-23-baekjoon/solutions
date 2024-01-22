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

for _ in range(int(stdin.readline())):
    cat_lovers, dog_lovers = [], []
    _, _, N = map(int, stdin.readline().split())
    for _ in range(N):
        q1, q2 = stdin.readline().split()
        a1, i1 = q1[0], int(q1[1:]) - 1
        a2, i2 = q2[0], int(q2[1:]) - 1
        if a1 == 'C' and a2 == 'D': cat_lovers.append((i1, i2))
        else: dog_lovers.append((i2, i1))  # a1 == 'D' and a2 == 'C'

    C, D = len(cat_lovers), len(dog_lovers)
    graph = [[] for _ in range(C)]
    for i in range(C):
        for j in range(D):
            if cat_lovers[i][0] == dog_lovers[j][0] or \
                    cat_lovers[i][1] == dog_lovers[j][1]:
                graph[i].append(j)

    matches = 0
    selected = [-1] * D
    for i in range(C):
        visited = [0] * C
        matches += dfs(i)
    print(N - matches)

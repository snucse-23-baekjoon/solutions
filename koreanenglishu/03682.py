from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
stdin = open("../input.txt", 'r')

def dfs(u):
    global vorder_counter, sccnum_counter
    vorder_root = vorder[u] = vorder_counter
    vorder_counter += 1
    stack.append(u)

    for v in graph[u]:
        if vorder[v] == -1:
            vorder_root = min(vorder_root, dfs(v))
        elif sccnum[v] == -1:
            vorder_root = min(vorder_root, vorder[v])

    if vorder_root == vorder[u]:
        while stack:
            v = stack.pop()
            sccnum[v] = sccnum_counter
            if u == v: break
        sccnum_counter += 1
    return vorder_root

for _ in range(int(stdin.readline())):
    n, m = map(int, stdin.readline().split())
    graph = [[] for _ in range(n)]
    for _ in range(m):
        s1, s2 = map(int, stdin.readline().split())
        graph[s1 - 1].append(s2 - 1)

    vorder_counter, sccnum_counter = 0, 0
    vorder, sccnum = [-1] * n, [-1] * n
    stack = []
    for u in range(n):
        if vorder[u] == -1: dfs(u)

    k = sccnum_counter
    in_deg_is_zero, out_deg_is_zero = [1] * k, [1] * k
    for u in range(n):
        for v in graph[u]:
            if sccnum[u] != sccnum[v]:
                in_deg_is_zero[sccnum[v]] = 0
                out_deg_is_zero[sccnum[u]] = 0

    print(max(
        sum(in_deg_is_zero), sum(out_deg_is_zero)
    ) if k > 1 else 0)

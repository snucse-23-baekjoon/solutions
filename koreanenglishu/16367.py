from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
stdin = open("../input.txt", 'r')

def dfs(u):
    global vorder_counter, sccnum_counter
    vorder_root = vorder[u] = vorder_counter
    vorder_counter += 1
    stack.append(u)

    for v in graph[u]:
        if not vorder[v]: vorder_root = min(vorder_root, dfs(v))
        elif not sccnum[v]: vorder_root = min(vorder_root, vorder[v])

    if vorder_root == vorder[u]:
        while stack:
            v = stack.pop()
            sccnum[v] = sccnum_counter
            if u == v: break
        sccnum_counter += 1
    return vorder_root


k, n = map(int, stdin.readline().split())
graph = [[] for _ in range(2 * k + 1)]

for _ in range(n):
    i1, c1, i2, c2, i3, c3 = stdin.readline().split()
    n1, n2, n3 = map(
        lambda i, c: int(i) * (1 if c == 'R' else -1),
        [i1, i2, i3], [c1, c2, c3]
    )
    graph[-n1].extend([n2, n3])
    graph[-n2].extend([n3, n1])
    graph[-n3].extend([n1, n2])

vorder, sccnum = [0] * (2 * k + 1), [0] * (2 * k + 1)
vorder_counter, sccnum_counter = 1, 1
stack = []

for i in range(1, 2 * k + 1):
    if not vorder[i]: dfs(i)

answer = []
for i in range(1, k + 1):
    if sccnum[i] < sccnum[-i]: answer.append('R')
    elif sccnum[i] > sccnum[-i]: answer.append('B')
    else: print(-1); exit()
print(''.join(answer))

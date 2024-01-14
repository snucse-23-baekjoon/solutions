from sys import stdin, setrecursionlimit
setrecursionlimit(100000)
stdin = open("../input.txt", 'r')

def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    check1 = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    check2 = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)
    return check1 <= 0 and check2 <= 0

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


segments = []
N = int(stdin.readline())
graph = [[] for _ in range(6 * N + 1)]

for i in range(1, 3 * N + 1):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    for j in range(1, i):
        x3, y3, x4, y4 = segments[j - 1]
        if intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            graph[-i].append(j); graph[-j].append(i)
    segments.append((x1, y1, x2, y2))

for i in range(1, 3 * N + 1, 3):
    for j, k in [(i, i + 1), (i + 1, i + 2), (i + 2, i)]:
        graph[j].append(-k); graph[k].append(-j)

vorder, sccnum = [0] * (6 * N + 1), [0] * (6 * N + 1)
vorder_counter, sccnum_counter = 1, 1
stack = []

for i in range(1, 6 * N + 1):
    if not vorder[i]: dfs(i)

sticks_to_remove = []
for i in range(1, 3 * N + 1):
    if sccnum[i] == sccnum[-i]: print(-1); exit()
    elif sccnum[i] < sccnum[-i]: sticks_to_remove.append(i)

print(len(sticks_to_remove))
print(*sticks_to_remove)

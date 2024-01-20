def bf(E):
    d = {i: 0 for i in range(1, n+1)}
    for i in range(n):
        for j in range(1, n+1):
            for e, t in E[j]:
                if d[e] > d[j] + t:
                    d[e] = d[j] + t
                    if i == n-1:
                        return 1
    return 0

from sys import stdin
import heapq
tc = int(stdin.readline())
for _ in range(tc):
    n, m, w = map(int, stdin.readline().split())
    E = {i: [] for i in range(1, n+1)}
    for __ in range(m):
        s, e, t = map(int, stdin.readline().split())
        E[s].append((e, t))
        E[e].append((s, t))
    for __ in range(w):
        s, e, t = map(int, stdin.readline().split())
        E[s].append((e, -t))
    if bf(E):
        print('YES')
    else:
        print('NO')
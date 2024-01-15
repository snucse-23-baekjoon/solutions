def f(lst):
    if not lst:
        return 1
    return (d[lst[0]] + 1) * f(lst[1:])

from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    d = dict()
    for __ in range(n):
        kind = stdin.readline().split()[1]
        if kind in d:
            d[kind] += 1
        else:
            d[kind] = 1
    lst = list(d.keys())
    print(f(lst) - 1)
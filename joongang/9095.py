def f(n):
    if n in d:
        return d[n]
    d[n] = f(n-1) + f(n-2) + f(n-3)
    return d[n]

from sys import stdin
t = int(stdin.readline())
d = {1:1, 2:2, 3:4, 4:7}
for _ in range(t):
    n = int(stdin.readline())
    print(f(n))
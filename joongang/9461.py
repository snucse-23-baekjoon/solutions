def f(n):
    if n not in d:
        d[n] = f(n-1) + f(n-5)
    return d[n]

from sys import stdin
t = int(stdin.readline())
d = {1:1, 2:1, 3:1, 4:2, 5:2, 6:3, 7:4, 8:5, 9:7, 10:9}
for _ in range(t):
    n = int(stdin.readline())
    print(f(n))
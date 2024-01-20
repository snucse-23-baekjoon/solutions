from sys import stdin
n, m = map(int, stdin.readline().split())
d = dict()
for _ in range(n):
    link, password = stdin.readline().rstrip().split()
    d[link] = password
for _ in range(m):
    link = stdin.readline().rstrip()
    print(d[link])
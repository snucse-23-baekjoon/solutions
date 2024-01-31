from sys import stdin
n, k = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
d = [0 for i in range(k+1)]
for w, v in lst:
    for i in range(k, w-1, -1):
        d[i] = max(d[i], d[i-w]+v)
print(d[k])
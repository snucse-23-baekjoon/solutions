from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [0]*(n+1)
for _ in range(m):
    x, y, z = map(int, stdin.readline().split())
    for i in range(x, y+1):
        lst[i] = z
print(*lst[1:])
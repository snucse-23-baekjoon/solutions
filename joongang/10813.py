from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [i for i in range(n+1)]
for _ in range(m):
    x, y = map(int, stdin.readline().split())
    lst[x], lst[y] = lst[y], lst[x]
print(*lst[1:])
from sys import stdin
n, m = map(int, stdin.readline().split())
lst = [i for i in range(n+1)]
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    lst = lst[:i] + list(reversed(lst[i:j+1])) + lst[j+1:]
print(*lst[1:])
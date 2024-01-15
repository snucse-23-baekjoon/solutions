from sys import stdin
n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
s = [0]
for i in range(n):
    s.append(s[i] + lst[i])
for _ in range(m):
    i, j = map(int, stdin.readline().split())
    print(s[j] - s[i-1])
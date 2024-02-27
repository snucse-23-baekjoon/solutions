from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    print(sum(map(int, stdin.readline().split())))
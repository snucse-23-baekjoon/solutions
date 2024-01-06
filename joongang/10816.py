from sys import stdin
n = int(stdin.readline())
cards = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))
d = dict()
for i in range(n):
    if cards[i] in d.keys():
        d[cards[i]] += 1
    else:
        d[cards[i]] = 1
for i in range(m):
    if targets[i] in d.keys():
        print(d[targets[i]], end=' ')
    else:
        print(0, end=' ')
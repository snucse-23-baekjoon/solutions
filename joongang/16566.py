def find(x):
    if x != uf[x]:
        uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[x] = y

from sys import stdin
from bisect import bisect_right
n, m, k = map(int, stdin.readline().split())
cards = list(map(int, stdin.readline().split()))
opponent = list(map(int, stdin.readline().split()))
cards.sort()
uf = [i for i in range(m)]
for i in opponent:
    idx = bisect_right(cards, i)
    idx = find(idx)
    print(cards[idx])
    if idx != m-1:
        union(idx, idx+1)
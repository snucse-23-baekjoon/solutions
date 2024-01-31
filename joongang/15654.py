from sys import stdin
from itertools import permutations
n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
lst.sort()
for i in permutations(lst, m):
    print(*i)
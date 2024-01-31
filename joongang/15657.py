from sys import stdin
from itertools import combinations_with_replacement
n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
lst.sort()
for i in combinations_with_replacement(lst, m):
    print(*i)
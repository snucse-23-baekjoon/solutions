from itertools import combinations_with_replacement
n, m = map(int, input().split())
lst = list(map(int, input().split()))
lst.sort()
s = set()
for i in combinations_with_replacement(lst, m):
    if i not in s:
        print(*i)
        s.add(i)
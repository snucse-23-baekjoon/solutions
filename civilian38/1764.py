import sys

dnum, bnum = tuple(map(int, sys.stdin.readline().split()))
dlist = [sys.stdin.readline().rstrip() for _ in range(dnum)]

bset = set()
for _ in range(bnum):
    bset.add(sys.stdin.readline().rstrip())

dblist = list()
for dperson in dlist:
    if dperson in bset:
        dblist.append(dperson)

print(len(dblist))
any(map(print, sorted(dblist)))
from sys import stdin
from bisect import bisect_left
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
lst.sort(key = lambda x: x[0])
d = [lst[0][1]]
idxlst = [0]*n
cnt = 1
for i in range(1, n):
    x, y = lst[i]
    if y > d[-1]:
        d.append(y)
        idxlst[i] = cnt
        cnt += 1
    else:
        idx = bisect_left(d, y)
        d[idx] = y
        idxlst[i] = idx
print(n-cnt)
findidx = n-1
notcross = set()
while cnt > 0:
    cnt -= 1
    while idxlst[findidx] != cnt:
        findidx -= 1
    notcross.add(findidx)
for i in range(n):
    if i not in notcross:
        print(lst[i][0])
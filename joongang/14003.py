from sys import stdin
from bisect import bisect_left
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
log = [0]*n
tmp = [lst[0]]
for i in range(1, n):
    if lst[i] > tmp[-1]:
        log[i] = len(tmp)
        tmp.append(lst[i])
    else:
        idx = bisect_left(tmp, lst[i])
        log[i] = idx
        tmp[idx] = lst[i]
cnt = len(tmp)
print(cnt)
cnt -= 1
target = tmp[-1]
idx = n-1
lis = [target]
while 1:
    if lst[idx] == target:
        cnt -= 1
        break
    idx -= 1
while cnt >= 0:
    if log[idx] == cnt:
        lis.append(lst[idx])
        cnt -= 1
    idx -= 1
lis.reverse()
print(*lis)
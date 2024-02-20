from sys import stdin
from bisect import bisect_left
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
lis = [lst[0]]
for i in range(1, n):
    if lst[i] > lis[-1]:
        lis.append(lst[i])
    else:
        idx = bisect_left(lis, lst[i])
        lis[idx] = lst[i]
print(len(lis))
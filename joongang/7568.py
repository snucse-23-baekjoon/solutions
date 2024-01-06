def comp(a, b):
    if a[0] > b[0] and a[1] > b[1]:
        return 1
    if a[0] < b[0] and a[1] < b[1]:
        return -1
    return 0

from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    lst.append(list(map(int, stdin.readline().split())))
ans = []
for i in range(n):
    cnt = 1
    for j in range(n):
        if i == j:
            pass
        if comp(lst[i], lst[j]) == -1:
            cnt += 1
    ans.append(cnt)
for i in ans:
    print(i, end=' ')
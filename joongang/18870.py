from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
sorted_lst = sorted(list(set(lst)))
d = {sorted_lst[i]: i for i in range(len(sorted_lst))}
for i in lst:
    print(d[i], end=' ')
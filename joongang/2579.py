def f(lst):
    global d
    n = len(lst)
    if n in d:
        return d[n]
    if n == 2:
        d[n] = sum(lst)
    elif n == 3:
        d[n] = max(lst[0], lst[1]) + lst[2]
    elif n == 4:
        d[n] = max([lst[0] + lst[2], lst[1], lst[0] + lst[1]]) + lst[3]
    else:
        d[n] = max(f(lst[:-3]) + lst[-2], f(lst[:-2])) + lst[-1]
    return d[n]

from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    lst.append(int(stdin.readline()))
d = {0: 0, 1: lst[0]}
print(f(lst))
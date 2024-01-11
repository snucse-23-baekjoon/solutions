def r(n):
    d = n - int(n)
    if d >= 0.5:
        return int(n)+1
    return int(n)

from sys import stdin
n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(int(stdin.readline()))
lst.sort()
cutnum = r(n * 0.15)
if not n:
    print(0)
else:
    print(r(sum(lst[cutnum:len(lst)-cutnum])/(n-2*cutnum)))
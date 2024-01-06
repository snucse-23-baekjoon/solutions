from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    a, b = stdin.readline().split()
    a = int(a)
    lst.append((a, b, i))
lst.sort(key = lambda x: (x[0], x[2]))
for i in lst:
    print(i[0], i[1])
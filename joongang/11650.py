from sys import stdin
n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, stdin.readline().split())))
lst.sort(key = lambda x: (x[0], x[1]))
for i in lst:
    print(i[0], i[1])
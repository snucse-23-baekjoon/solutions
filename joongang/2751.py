from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    lst.append(int(stdin.readline()))
lst.sort()
for i in range(n):
    print(lst[i])
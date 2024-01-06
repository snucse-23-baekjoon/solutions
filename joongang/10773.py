from sys import stdin
k = int(stdin.readline())
lst = []
for i in range(k):
    n = int(stdin.readline())
    if n == 0:
        lst.pop()
    else:
        lst.append(n)
print(sum(lst))
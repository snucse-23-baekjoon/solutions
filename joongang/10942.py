from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
d = [[0]*n for i in range(n)]
for i in range(n):
    d[i][i] = 1
    if i != n-1 and lst[i] == lst[i+1]:
        d[i][i+1] = 1
for i in range(m):
    s, e = map(int, stdin.readline().split())
    stack = [(s, e)]
    while s <= e:
        if d[s-1][e-1]:
            for l, r in stack:
                d[l-1][r-1] = 1
            print(1)
            break
        if lst[s-1] == lst[e-1]:
            s += 1
            e -= 1
            stack.append((s, e))
        else:
            print(0)
            break
    if s > e:
        print(0)
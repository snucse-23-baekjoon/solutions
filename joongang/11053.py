from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
d = [[1, lst[0]]]
for i in range(1, n):
    tmp = [1, lst[i]]
    for j in range(i):
        if d[j][1] < lst[i]:
            tmp[0] = max(tmp[0], d[j][0] + 1)
    d.append(tmp)
d.sort(key = lambda x: x[0])
print(d[-1][0])
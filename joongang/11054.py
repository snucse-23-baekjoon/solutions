from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
d1 = [[1, lst[0]]]
for i in range(1, n):
    tmp = [1, lst[i]]
    for j in range(i):
        if d1[j][1] < lst[i]:
            tmp[0] = max(tmp[0], d1[j][0] + 1)
    d1.append(tmp)
lst.reverse()
d2 = [[1, lst[0]]]
for i in range(1, n):
    tmp = [1, lst[i]]
    for j in range(i):
        if d2[j][1] < lst[i]:
            tmp[0] = max(tmp[0], d2[j][0] + 1)
    d2.append(tmp)
d2.reverse()
ans = 0
for i in range(n):
    ans = max(ans, d1[i][0] + d2[i][0])
print(ans-1)
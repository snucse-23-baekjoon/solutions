from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
tmp = lst[0]
for i in range(1, n):
    tmp = [lst[i][0] + min(tmp[1], tmp[2]), lst[i][1] + min(tmp[0], tmp[2]), lst[i][2] + min(tmp[0], tmp[1])]
print(min(tmp))
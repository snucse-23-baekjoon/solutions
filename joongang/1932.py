from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
tmp = lst[0]
for i in range(1, n):
    tmp2 = lst[i]
    for j in range(i+1):
        if j == 0:
            tmp2[j] += tmp[0]
        elif j == i:
            tmp2[j] += tmp[i-1]
        else:
            tmp2[j] += max(tmp[j-1], tmp[j])
    tmp = tmp2[:]
print(max(tmp))
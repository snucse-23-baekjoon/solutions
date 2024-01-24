from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    lst = [list(map(int, stdin.readline().split())) for i in range(2)]
    if n == 1:
        print(max(lst[0][0], lst[1][0]))
        continue
    tmp = [lst[1][0] + lst[0][1], lst[0][0] + lst[1][1]]
    tmp2 = [lst[0][0], lst[1][0]]
    for i in range(2, n):
        tmp3 = tmp.copy()
        tmp = [max(tmp[1], tmp2[1])+lst[0][i], max(tmp[0], tmp2[0])+lst[1][i]]
        tmp2 = tmp3.copy()
    print(max(tmp))

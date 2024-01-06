from sys import stdin
t = int(stdin.readline())
lst = [[0 for j in range(14)] for i in range(15)]
lst[0] = [i for i in range(1, 15)]
for i in range(1, 15):
    lst[i][0] = 1
    for j in range(1, 14):
        lst[i][j] = lst[i][j-1] + lst[i-1][j]
for i in range(t):
    k = int(stdin.readline())
    n = int(stdin.readline())
    print(lst[k][n-1])
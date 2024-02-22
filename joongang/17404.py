from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
d = [[[0]*3 for i in range(3)] for i in range(n)]
d[0] = [[lst[0][i]]*3 for i in range(3)]
d[1][0] = [float('inf'), lst[0][0]+lst[1][1], lst[0][0]+lst[1][2]]
d[1][1] = [lst[0][1]+lst[1][0], float('inf'), lst[0][1]+lst[1][2]]
d[1][2] = [lst[0][2]+lst[1][0], lst[0][2]+lst[1][1], float('inf')]
for i in range(2, n):
    for j in range(3):
        d[i][j][0] = min(d[i-1][j][1], d[i-1][j][2]) + lst[i][0]
        d[i][j][1] = min(d[i-1][j][0], d[i-1][j][2]) + lst[i][1]
        d[i][j][2] = min(d[i-1][j][0], d[i-1][j][1]) + lst[i][2]
print(min([d[n-1][0][1], d[n-1][0][2], d[n-1][1][0], d[n-1][1][2], d[n-1][2][0], d[n-1][2][1]]))
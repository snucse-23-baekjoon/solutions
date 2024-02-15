def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2-x1)*(y3-y1) - (x3-x1)*(y2-y1)
    if tmp>0:
        return 1
    elif tmp<0:
        return -1
    else:
        return 0

def triarea(x1, y1, x2, y2, x3, y3):
    return ccw(x1, y1, x2, y2, x3, y3)*abs((x2-x1)*(y3-y1) - (x3-x1)*(y2-y1))/2

from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
ans = 0
for i in range(1, n-1):
    ans += triarea(*(lst[0]+lst[i]+lst[i+1]))
print(round(abs(ans), 1))
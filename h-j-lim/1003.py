import sys


T = int(input())
for i in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(sys.stdin.readline())
    count = 0
    for j in range(n):
        c_x, c_y, r = map(int, sys.stdin.readline().split())
        dist_1 = ((c_x - x1) ** 2 + (c_y - y1) ** 2) ** (1/2)
        dist_2 = ((c_x - x2) ** 2 + (c_y - y2) ** 2) ** (1/2)
        if (dist_1 - r) * (dist_2 - r) < 0:
            count += 1
    print(count)

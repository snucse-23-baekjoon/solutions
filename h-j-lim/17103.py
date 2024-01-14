import sys


T = int(input())
for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dist = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** (1/2)
    if dist == 0:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        if dist > r1 + r2:
            print(0)
        elif dist == r1 + r2:
            print(1)
        else:
            if abs(r1 - r2) < dist:
                print(2)
            elif abs(r1 - r2) == dist:
                print(1)
            else:
                print(0)

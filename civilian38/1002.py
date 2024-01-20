def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

import sys

repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    x1, y1, r1, x2, y2, r2 = tuple(map(int, sys.stdin.readline().split()))
    dist = distance((x1, y1), (x2, y2))
    if (x1, y1) == (x2, y2) and r1 == r2:
        print(-1)
    else:
        if max(r1, r2) < dist:
            if r1 + r2 > dist:
                print(2)
            elif r1 + r2 == dist:
                print(1)
            else:
                print(0)
        elif max(r1, r2) == dist:
            print(2)
        else:
            if abs(r1 - r2) < dist:
                print(2)
            elif abs(r1 - r2) == dist:
                print(1)
            else:
                print(0)
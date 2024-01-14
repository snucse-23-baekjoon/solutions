from sys import stdin
import math
stdin = open("../input.txt", 'r')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        outer_product = x1 * y2 - x2 * y1
        if outer_product == 0:
            dist_self = x1 * x1 + y1 * y1
            dist_other = x2 * x2 + y2 * y2
            return dist_self < dist_other
        else:
            return outer_product > 0

def convex_hull(points):
    points = sorted(points, key=lambda p: (p.x, p.y))
    origin_x, origin_y = points[0].x, points[0].y

    for p in points:
        p.x -= origin_x
        p.y -= origin_y

    points.sort()
    shell = points[:2]

    for p in points[2:]:
        while True:
            a, b = shell[-2], shell[-1]
            outer_product = (b.x - a.x) * \
                (p.y - b.y) - (b.y - a.y) * (p.x - b.x)
            if outer_product <= 0:
                shell.pop()
            if outer_product >= 0:
                shell.append(p)
                break

    for p in shell:
        p.x += origin_x
        p.y += origin_y

    return shell

def rotating_calipers(shell):
    m = len(shell)
    dist_max = 0
    a, a_max, b, b_max = 0, 0, 1, 1

    while True:
        x = shell[b].x - shell[a].x
        y = shell[b].y - shell[a].y
        if dist_max < x * x + y * y:
            dist_max = x * x + y * y
            a_max, b_max = a, b

        a_, b_ = (a + 1) % m, (b + 1) % m
        x1 = shell[a_].x - shell[a].x
        y1 = shell[a_].y - shell[a].y
        x2 = shell[b_].x - shell[b].x
        y2 = shell[b_].y - shell[b].y

        outer_product = x1 * y2 - x2 * y1
        if outer_product > 0:
            b = b_
        else:
            if a == m - 1:
                break
            a = a_

    return shell[a_max], shell[b_max]

for _ in range(int(stdin.readline())):
    points = []
    n = int(stdin.readline())

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        points.append(Point(x, y))

    shell = convex_hull(points)
    p, q = rotating_calipers(shell)
    print(p.x, p.y, q.x, q.y)

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

points = []
n, l = map(int, stdin.readline().split())

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    points.append(Point(x, y))

shell = convex_hull(points)
total_length = 0.0

for i in range(len(shell)):
    a, b, c = shell[i - 2], shell[i - 1], shell[i]
    x1, y1 = a.x - b.x, a.y - b.y
    x2, y2 = c.x - b.x, c.y - b.y
    dist1 = math.sqrt(x1 * x1 + y1 * y1)
    dist2 = math.sqrt(x2 * x2 + y2 * y2)
    angle = math.acos(
        (x1 * x2 + y1 * y2) / (dist1 * dist2)
    )
    total_length += dist1 + l * (math.pi - angle)

print(round(total_length))

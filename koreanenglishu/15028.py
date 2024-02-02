import sys
import math
sys.stdin = open("../input.txt", 'r')


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        outer_product = self.x * other.y - self.y * other.x
        if outer_product == 0:
            dist_self = self.x ** 2 + self.y ** 2
            dist_other = other.x ** 2 + other.y ** 2
            return dist_self < dist_other
        else:
            return outer_product > 0

    def dist(self, other1, other2):
        ax, ay = self.x - other2.x, self.y - other2.y
        bx, by = other1.x - other2.x, other1.y - other2.y
        a_square = ax ** 2 + ay ** 2
        b_square = bx ** 2 + by ** 2
        inner_product = ax * bx + ay * by
        if a_square == 0:
            return 0
        else:
            return math.sqrt(a_square - (inner_product ** 2) / b_square)


n = int(sys.stdin.readline())

vertex = []
x_origin, y_origin = 100000, -100000
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    vertex.append(Point(x, y))
    if x_origin > x:
        x_origin, y_origin = x, y
    elif x_origin == x and y_origin < y:
        y_origin = y

for point in vertex:
    point.x -= x_origin
    point.y -= y_origin

vertex.sort()
convex_hull = vertex[:2]
for point in vertex[2:]:
    while True:
        a, b, c = convex_hull[-2], convex_hull[-1], point
        outer_product = (b.x - a.x) * (c.y - b.y) - (b.y - a.y) * (c.x - b.x)
        if outer_product < 0:
            convex_hull.pop()
        elif outer_product > 0:
            convex_hull.append(point)
            break
        else:
            convex_hull.pop()
            convex_hull.append(point)
            break

min_width = 10000.0
for i in range(len(convex_hull)):
    max_dist = 0.0
    a, b = convex_hull[i - 1], convex_hull[i]
    for point in convex_hull:
        max_dist = max(max_dist, point.dist(a, b))
    min_width = min(min_width, max_dist)

print(min_width)

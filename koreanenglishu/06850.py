from sys import stdin
stdin = open("../input.txt", 'r')

class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __lt__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        outer_product = x1 * y2 - x2 * y1
        if outer_product == 0:
            dist_self = x1 * x1 + y1 * y1
            dist_other = x2 * x2 + y2 * y2
            return dist_self < dist_other
        else: return outer_product > 0

def convex_hull(points):
    points = sorted(points, key=lambda p: (p.x, p.y))
    origin_x, origin_y = points[0].x, points[0].y
    for p in points: p.x -= origin_x; p.y -= origin_y
    points.sort()

    shell = points[:2]
    for p in points[2:]:
        while True:
            a, b = shell[-2], shell[-1]
            outer_product = (b.x - a.x) * (p.y - b.y) - \
                            (b.y - a.y) * (p.x - b.x)
            if outer_product <= 0: shell.pop()
            if outer_product >= 0: shell.append(p); break
    for p in shell: p.x += origin_x; p.y += origin_y
    return shell

points = []
for _ in range(int(stdin.readline())):
    points.append(Point(*map(int, stdin.readline().split())))
shell = convex_hull(points)

sum_of_outer_products = 0
for i in range(len(shell)):
    a, b = shell[i - 1], shell[i]
    sum_of_outer_products += a.x * b.y - b.x * a.y
print(sum_of_outer_products // 100)

from sys import stdin
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

# WARNING: convex hull is removed from the original points
def convex_hull(points):
    points.sort(key=lambda p: (p.x, p.y))
    origin_x = points[0].x
    origin_y = points[0].y

    for p in points:
        p.x -= origin_x
        p.y -= origin_y

    points.sort()
    shell = points[:2]
    indexes = [0, 1]

    for i in range(2, len(points)):
        p = points[i]
        while True:
            a, b = shell[-2], shell[-1]
            outer_product = (b.x - a.x) * \
                (p.y - b.y) - (b.y - a.y) * (p.x - b.x)
            if outer_product <= 0:
                shell.pop()
                indexes.pop()
            if outer_product >= 0:
                shell.append(p)
                indexes.append(i)
                break

    for i in reversed(indexes):
        del points[i]

    for p in points:
        p.x += origin_x
        p.y += origin_y

    for p in shell:
        p.x += origin_x
        p.y += origin_y

    return shell

def check_inside(shell, point):
    origin_x = shell[0].x
    origin_y = shell[0].y
    point.x -= origin_x
    point.y -= origin_y

    for p in shell:
        p.x -= origin_x
        p.y -= origin_y

    left, right = 0, len(shell)
    while right - left > 1:
        center = (left + right + 1) // 2
        if point < shell[center]:
            right = center
        else:
            left = center

    a, b = shell[left], shell[right % len(shell)]
    x1, y1 = a.x - point.x, a.y - point.y
    x2, y2 = b.x - point.x, b.y - point.y
    outer_product = x1 * y2 - x2 * y1

    point.x += origin_x
    point.y += origin_y

    return outer_product > 0

n, px, py = map(int, stdin.readline().split())
point = Point(px, py)
points = []

for _ in range(n):
    x, y = map(int, stdin.readline().split())
    points.append(Point(x, y))

count = 0
while len(points) > 2:
    shell = convex_hull(points)

    # for p in shell:
    #     print(p.x, p.y)
    # print()
    # for p in points:
    #     print(p.x, p.y)

    if not check_inside(shell, point):
        break
    count += 1

print(count)

from sys import stdin
stdin = open("../input.txt", 'r')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        if y1 * x2 == x1 * y2:
            return x1 * x1 + y1 * y1 < x2 * x2 + y2 * y2
        return y1 * x2 < x1 * y2

points = []
for _ in range(int(stdin.readline())):
    x, y, c = stdin.readline().split()
    if c == 'Y':
        points.append((int(x), int(y)))

points.sort()
o = points[0]
points = list(map(
    lambda p: Point(p[0] - o[0], p[1] - o[1]), points
))
points.sort()

for i in range(len(points) - 2):
    p1, p2, p3 = points[i:i + 3]
    if (p2.x - p1.x) * (p3.y - p1.y) < \
            (p2.y - p1.y) * (p3.x - p1.x):
        points[i + 1:] = list(reversed(points[i + 1:]))

print(len(points))
for p in points:
    print(p.x + o[0], p.y + o[1])

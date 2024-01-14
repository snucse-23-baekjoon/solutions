from sys import stdin
stdin = open("../input.txt", 'r')

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        x1, y1 = self.x, self.y
        x2, y2 = other.x, other.y
        out_prod = x1 * y2 - x2 * y1
        if out_prod == 0:
            dist_self = x1 * x1 + y1 * y1
            dist_other = x2 * x2 + y2 * y2
            return dist_self < dist_other
        else:
            return out_prod > 0

def convex_hull(points):
    if len(points) < 3:
        return points[:]

    points = sorted(
        points, key=lambda p: (p.x, p.y)
    )
    origin_x = points[0].x
    origin_y = points[0].y

    for p in points:
        p.x -= origin_x
        p.y -= origin_y

    points.sort()
    shell = points[:2]

    for p in points[2:]:
        while True:
            a, b = shell[-2], shell[-1]
            out_prod = \
                (b.x - a.x) * (p.y - b.y) \
                - (b.y - a.y) * (p.x - b.x)
            if out_prod <= 0:
                shell.pop()
            if out_prod >= 0:
                shell.append(p)
                break

    for p in shell:
        p.x += origin_x
        p.y += origin_y

    return shell

def check_ccw(p1, p2, p3):
    x1, y1 = p2.x - p1.x, p2.y - p1.y
    x2, y2 = p3.x - p1.x, p3.y - p1.y
    return x1 * y2 - x2 * y1

def check_intersect(p1, p2, p3, p4):
    check_1 = check_ccw(p1, p2, p3) * check_ccw(p1, p2, p4)
    check_2 = check_ccw(p3, p4, p1) * check_ccw(p3, p4, p2)

    if check_1 == 0 and check_2 == 0:
        if (p1.x, p1.y) > (p2.x, p2.y):
            p1, p2 = p2, p1
        if (p3.x, p3.y) > (p4.x, p4.y):
            p3, p4 = p4, p3
        return (p3.x, p3.y) <= (p2.x, p2.y) \
            and (p1.x, p1.y) <= (p4.x, p4.y)

    return check_1 <= 0 and check_2 <= 0

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
    out_prod = x1 * y2 - x2 * y1

    point.x += origin_x
    point.y += origin_y
    for p in shell:
        p.x += origin_x
        p.y += origin_y

    return out_prod >= 0

for _ in range(int(stdin.readline())):
    black, white = [], []
    n, m = map(int, stdin.readline().split())

    for _ in range(n):
        x, y = map(int, stdin.readline().split())
        black.append(Point(x, y))
    for _ in range(m):
        x, y = map(int, stdin.readline().split())
        white.append(Point(x, y))

    shell_black = convex_hull(black)
    shell_white = convex_hull(white)

    if len(shell_black) > len(shell_white):
        shell_temp = shell_black
        shell_black = shell_white
        shell_white = shell_temp

    separable = True
    if len(shell_white) == 1:
        pass

    elif len(shell_white) == 2:
        if len(shell_black) == 1:
            b = shell_black[0]
            w1, w2 = shell_white
            x1, y1 = w1.x - b.x, w1.y - b.y
            x2, y2 = w2.x - b.x, w2.y - b.y
            len1_sq = x1 * x1 + y1 * y1
            len2_sq = x2 * x2 + y2 * y2
            in_prod = x1 * x2 + y1 * y2
            if in_prod * in_prod == len1_sq * \
                    len2_sq and in_prod < 0:
                separable = False

        else:  # len(shell_black) == 2
            b1, b2 = shell_black
            w1, w2 = shell_white
            if check_intersect(b1, b2, w1, w2):
                separable = False

    else:  # len(shell_white) > 2
        if len(shell_black) == 1:
            b = shell_black[0]
            if check_inside(shell_white, b):
                separable = False

        elif len(shell_black) == 2:
            b1, b2 = shell_black
            for i in range(len(shell_white)):
                w1 = shell_white[i - 1]
                w2 = shell_white[i]
                if check_intersect(b1, b2, w1, w2):
                    separable = False
                    break

        else:  # len(shell_black) > 2
            for i in range(len(shell_black)):
                b1 = shell_black[i - 1]
                b2 = shell_black[i]
                for j in range(len(shell_white)):
                    w1 = shell_white[j - 1]
                    w2 = shell_white[j]
                    if check_intersect(b1, b2, w1, w2):
                        separable = False
                        break
                if not separable:
                    break
            if separable:
                b = shell_black[0]
                w = shell_white[0]
                if check_inside(shell_black, w) or \
                        check_inside(shell_white, b):
                    separable = False

    print("YES" if separable else "NO")

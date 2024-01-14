from sys import stdin
stdin = open("../input.txt", 'r')

def closest(left, right):
    if right - left == 2:
        x1, y1 = points_x[left]
        x2, y2 = points_x[left + 1]
        return (x2 - x1) ** 2 + (y2 - y1) ** 2

    if right - left == 3:
        x1, y1 = points_x[left]
        x2, y2 = points_x[left + 1]
        x3, y3 = points_x[left + 2]
        return min(
            (x2 - x1) ** 2 + (y2 - y1) ** 2,
            (x3 - x2) ** 2 + (y3 - y2) ** 2,
            (x1 - x3) ** 2 + (y1 - y3) ** 2
        )

    center = (left + right + 1) // 2
    dist_sq_min = min(
        closest(left, center),
        closest(center, right)
    )

    points_temp = []
    for p in points_x[left:right]:
        if (p[0] - points_x[center][0]) ** 2 < dist_sq_min:
            points_temp.append(p)
    points_temp.sort(key=lambda x: x[1])

    for i in range(len(points_temp)):
        x1, y1 = points_temp[i]
        for x2, y2 in points_temp[i + 1:i + 8]:
            if (y2 - y1) ** 2 >= dist_sq_min:
                break
            dist_sq_min = min(
                dist_sq_min,
                (x2 - x1) ** 2 + (y2 - y1) ** 2
            )

    return dist_sq_min

points = []
n = int(stdin.readline())
for _ in range(n):
    points.append(
        tuple(map(int, stdin.readline().split()))
    )

points_x = sorted(points, key=lambda p: p[0])

print(closest(0, n))

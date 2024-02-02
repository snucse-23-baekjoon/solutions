import sys
sys.setrecursionlimit(1_000_000)
sys.stdin = open("../input.txt", 'r')

def parallel(ax, ay, bx, by):
    in_prod = ax * bx + ay * by
    a_len_sq = ax * ax + ay * ay
    b_len_sq = bx * bx + by * by
    return in_prod * in_prod == a_len_sq * b_len_sq

def check_direction(ax, ay, bx, by, cx, cy):
    # CCW or CW check
    out_prod_ba = bx * ay - ax * by
    out_prod_bc = bx * cy - cx * by
    if out_prod_ba * out_prod_bc < 0:
        return False

    # sign check before squaring
    in_prod_ba = bx * ax + by * ay
    in_prod_bc = bx * cx + by * cy
    if in_prod_bc <= 0 <= in_prod_ba and in_prod_bc < in_prod_ba:
        return True
    if in_prod_ba <= 0 <= in_prod_bc and in_prod_ba < in_prod_bc:
        return False

    # square and compare magnitude
    a_len_sq = ax * ax + ay * ay
    c_len_sq = cx * cx + cy * cy
    if in_prod_ba >= 0 and in_prod_bc >= 0:
        return in_prod_ba * in_prod_ba * c_len_sq > in_prod_bc * in_prod_bc * a_len_sq
    if in_prod_ba <= 0 and in_prod_bc <= 0:
        return in_prod_ba * in_prod_ba * c_len_sq < in_prod_bc * in_prod_bc * a_len_sq

def intersect(x1, y1, x2, y2, x3, y3, x4, y4):
    parallel123 = parallel(x3 - x1, y3 - y1, x3 - x2, y3 - y2)
    parallel124 = parallel(x4 - x1, y4 - y1, x4 - x2, y4 - y2)
    parallel134 = parallel(x4 - x1, y4 - y1, x4 - x3, y4 - y3)
    parallel234 = parallel(x4 - x2, y4 - y2, x4 - x3, y4 - y3)

    # all points are on a line
    if all([parallel123, parallel124, parallel134, parallel234]):
        x12_min, x12_max = min(x1, x2), max(x1, x2)
        y12_min, y12_max = min(y1, y2), max(y1, y2)
        x34_min, x34_max = min(x3, x4), max(x3, x4)
        y34_min, y34_max = min(y3, y4), max(y3, y4)
        return x12_max >= x34_min and x34_max >= x12_min and y12_max >= y34_min and y34_max >= y12_min

    # exactly one point is out of line
    elif parallel123:
        x12_min, x12_max = min(x1, x2), max(x1, x2)
        y12_min, y12_max = min(y1, y2), max(y1, y2)
        return x12_min <= x3 <= x12_max and y12_min <= y3 <= y12_max
    elif parallel124:
        x12_min, x12_max = min(x1, x2), max(x1, x2)
        y12_min, y12_max = min(y1, y2), max(y1, y2)
        return x12_min <= x4 <= x12_max and y12_min <= y4 <= y12_max
    elif parallel134:
        x34_min, x34_max = min(x3, x4), max(x3, x4)
        y34_min, y34_max = min(y3, y4), max(y3, y4)
        return x34_min <= x1 <= x34_max and y34_min <= y1 <= y34_max
    elif parallel234:
        x34_min, x34_max = min(x3, x4), max(x3, x4)
        y34_min, y34_max = min(y3, y4), max(y3, y4)
        return x34_min <= x2 <= x34_max and y34_min <= y2 <= y34_max

    # no three points are on a line
    else:
        check1 = check_direction(x2 - x1, y2 - y1, x3 - x1, y3 - y1, x4 - x1, y4 - y1)
        check2 = check_direction(x1 - x2, y1 - y2, x3 - x2, y3 - y2, x4 - x2, y4 - y2)
        return check1 and check2

def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]

def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x <= y:
        parents[y] = x
    else:
        parents[x] = y

N = int(sys.stdin.readline())
coordinates = []
parents = [i for i in range(N)]

for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    coordinates.append((x1, y1, x2, y2))

for i in range(1, N):
    x1, y1, x2, y2 = coordinates[i]
    for j in range(i):
        x3, y3, x4, y4 = coordinates[j]
        if intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            union(parents, i, j)

lines = [0 for i in range(N)]
for i in range(N):
    find(parents, i)
for p in parents:
    lines[p] += 1

num_groups = 0
max_lines = 0
for l in lines:
    if l != 0:
        num_groups += 1
    if max_lines < l:
        max_lines = l
print(num_groups, max_lines, sep='\n')

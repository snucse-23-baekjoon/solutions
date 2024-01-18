W, H, f, c, x1, y1, x2, y2 = map(int, input().split())

if 2 * f > W:
    if f + x1 > W:
        width = x2 - x1
    elif f + x2 > W:
        width = (f + x2 - W) + 2 * (W - f - x1)
    else:
        width = 2 * (x2 - x1)
else:
    if x1 > f:
        width = x2 - x1
    elif x2 > f:
        width = (x2 - f) + 2 * (f - x1)
    else:
        width = 2 * (x2 - x1)
area_colored = width * (y2 - y1) * (c + 1)
print(W * H - area_colored)

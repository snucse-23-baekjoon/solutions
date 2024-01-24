x, y, c = map(eval, input().split())
l, r = 0, min(x, y)
mid = (l + r) / 2
h1 = (x ** 2 - mid ** 2) ** 0.5
h2 = (y ** 2 - mid ** 2) ** 0.5
for _ in range(10000):
    if c * (h1 + h2) == h1 * h2:
        break
    elif c * (h1 + h2) > h1 * h2:
        r = mid
    else:
        l = mid
    mid = (l + r) / 2
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5
print(mid)

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


x1, x2 = map(int, input().split())
y1, y2 = map(int, input().split())
z1 = x1 * y2 + y1 * x2
z2 = x2 * y2
print((z1 // gcd(z1, z2)), (z2 // gcd(z1, z2)))

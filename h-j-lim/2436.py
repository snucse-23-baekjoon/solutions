def gcd(a, b):
    if b > a:
        a, b = b, a
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


f, m = map(int, input().split())
num = m // f
ans = 0
for x in range(1, int(num ** 0.5) + 1):
    if num % x == 0:
        y = num // x
        if gcd(x, y) == 1:
            ans = x
print(f * ans, f * (num // ans))


def gcd(a, b):
    r = b % a
    if r == 0:
        return a
    return gcd(r, a)

a, b = map(int, input().split())
print(gcd(a, b))
print(a*b//gcd(a, b))
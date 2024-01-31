def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


A, B = map(int, input().split())
print('1' * gcd(A, B))

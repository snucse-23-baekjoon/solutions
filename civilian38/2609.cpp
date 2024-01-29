def gcd(num1, num2):
    a, b = max(num1, num2), min(num1, num2)
    if not a % b:
        return b
    else:
        return gcd(a % b, b)

a, b = tuple(map(int, input().split()))

print(gcd(a, b))
print(gcd(a, b) * (a // gcd(a, b)) * (b // gcd(a, b)))
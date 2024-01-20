def func(a, b, c):
    if b == 1:
        return a % c
    if b % 2 == 0:
        return (func(a % c, b // 2, c) ** 2) % c
    if b % 2 == 1:
        return ((func(a % c, b // 2, c) ** 2) * (a % c)) % c


A, B, C = map(int, input().split())
print(func(A, B, C))

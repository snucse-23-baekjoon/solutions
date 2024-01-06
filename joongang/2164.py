def f(n):
    if n == 1:
        return 1
    if not n % 2:
        return 2 * f(n//2)
    a = f(n-1)
    a = a+2 if a != n-1 else 2
    return a

n = int(input())
print(f(n))
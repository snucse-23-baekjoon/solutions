def f(a, b):
    if b == 1:
        return a%c
    tmp = f(a, b//2)
    if b % 2:
        return (tmp*tmp*a) % c
    else:
        return (tmp*tmp) % c

a, b, c = map(int, input().split())
print(f(a, b))
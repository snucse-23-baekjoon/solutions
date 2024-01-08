def f(n, r, c):
    if (r, c) == (0, 0):
        return 0
    if (r, c) == (0, 1):
        return 1
    if (r, c) == (1, 0):
        return 2
    if (r, c) == (1, 1):
        return 3
    if r < 2**(n-1) and c < 2**(n-1):
        return f(n-1, r, c)
    if r < 2**(n-1) and c >= 2**(n-1):
        return 4**(n-1) + f(n-1, r, c-2**(n-1))
    if r >= 2**(n-1) and c < 2**(n-1):
        return 2*(4**(n-1)) + f(n-1, r-2**(n-1), c)
    if r >= 2**(n-1) and c >= 2**(n-1):
        return 3*(4**(n-1)) + f(n-1, r-2**(n-1), c-2**(n-1))
n, r, c = map(int, input().split())
print(f(n, r, c))
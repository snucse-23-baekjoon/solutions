def f(n):
    if not n in d:
        d[n] = f(n-1) + f(n-2)*2
    return d[n]

n = int(input())
d = {1: 1, 2: 3}
print(f(n)%10007)
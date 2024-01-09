def f(n):
    global d
    if n in d:
        return d[n]
    if n % 6 == 0:
        d[n] = min(f(n//3), f(n//2)) + 1
    elif n % 3 == 0:
        d[n] = min(f(n//3), f(n-1)) + 1
    elif n % 2 == 0:
        d[n] = min(f(n//2), f(n-1)) + 1
    else:
        d[n] = f(n-1) + 1
    return d[n]
    
n = int(input())
d = {1: 0, 2: 1, 3: 1}
print(f(n))
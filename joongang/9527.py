def f(x):
    b = bin(x)[2:]
    l = len(b)
    cnt = 0
    for i in range(l):
        if b[i] == '1':
            p = l - i - 1
            cnt += d[p]
            cnt += x - 2**p + 1
            x -= 2**p
    return cnt

from sys import stdin
a, b = map(int, stdin.readline().split())
d = [0]*55
for i in range(1, 55):
    d[i] = 2**(i-1) + 2*d[i-1]
print(f(b)-f(a-1))
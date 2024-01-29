def power(x, n):
    if n == 1:
        return x
    tmp = power(x, n//2)
    if n%2:
        return (tmp*tmp*x)%X
    return (tmp*tmp)%X

from sys import stdin
import math
X = 1000000007
m = int(stdin.readline())
s = 0
for i in range(m):
    x, y = map(int, stdin.readline().split())
    gcd = math.gcd(x, y)
    x //= gcd
    y //= gcd
    s = (s + (y*power(x, X-2)))%X
print(s)
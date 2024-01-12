def gcd(a, b):
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b, r)

from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    m, n, x, y = map(int, stdin.readline().split())
    ans = x
    a, b = x, (ans - 1) % n + 1
    lcm = m*n/gcd(m, n)
    while b != y:
        ans += m
        b = (ans - 1) % n + 1
        if ans > lcm:
            ans = -1
            break
    print(ans)
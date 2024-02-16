import sys


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    if a % b == 0:
        return b
    return gcd(b, a % b)


T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())
    if y == N:
        y = 0
    lcm = (M * N) // gcd(M, N)
    i = 0
    find = False
    while i <= lcm // M:
        tmp = i * M + x
        if tmp % N == y:
            find = True
            break
        i += 1
    if find:
        print(i * M + x)
    else:
        print(-1)


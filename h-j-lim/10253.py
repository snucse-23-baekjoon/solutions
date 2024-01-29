import sys


def gcd(a, b):
    if a < b:
        return gcd(b, a)
    if b == 0:
        return a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


def henry(a, b):
    if (b / a) % 1 == 0:
        return b // a
    else:
        to_sub = b // a + 1
        a_new = a * to_sub - b
        b_new = b * to_sub
        to_div = gcd(a_new, b_new)
        a_new = a_new // to_div
        b_new = b_new // to_div
        return henry(a_new, b_new)


T = int(sys.stdin.readline())
for _ in range(T):
    A, B = map(int, sys.stdin.readline().split())
    print(henry(A, B))

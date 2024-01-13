import sys


def primecheck(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    else:
        for i in range(2, int(n ** (1/2)) + 1):
            if n % i == 0:
                return False
        return True


T = int(input())
for j in range(T):
    N = int(sys.stdin.readline())
    while not primecheck(N):
        N += 1
    print(N)

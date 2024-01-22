def power(n, k):
    if k == 0:
        return 1
    elif k % 2 == 0:
        return (power(n, k // 2) * power(n, k // 2)) % 10007
    else:
        return (power(n, k // 2) * power(n, k // 2) * n) % 10007


N = int(input())
if N == 0:
    print(0)
elif N == 1:
    print(1)
else:
    if N % 3 == 0:
        print(power(3, N // 3))
    elif N % 3 == 1:
        print((power(3, N // 3 - 1) * 4) % 10007)
    else:
        print((power(3, N // 3) * 2) % 10007)

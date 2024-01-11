def decompsum(n):
    s = n
    while n:
        s += n % 10
        n = n // 10
    return s


N = int(input())
f = 0
for i in range(1, N + 1):
    if decompsum(i) == N:
        print(i)
        f = 1
        break
if f == 0:
    print(0)

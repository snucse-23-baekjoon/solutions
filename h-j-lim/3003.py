n = int(input())
for i in range(1, 2 * n):
    a = n - abs(i - n)
    print(" " * (n - a) + "*" * (2 * a - 1))
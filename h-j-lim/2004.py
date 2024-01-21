def func(x, y):
    c = 0
    while x:
        x = x // y
        c += x
    return c


n, m = map(int, input().split())
count_5 = func(n, 5) - func(n - m, 5) - func(m, 5)
count_2 = func(n, 2) - func(n - m, 2) - func(m, 2)
print(min(count_2, count_5))

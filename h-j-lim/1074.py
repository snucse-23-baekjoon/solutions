N, r, c = map(int, input().split())
ans = 0
while N:
    x = 2 ** (N - 1)
    if r < x and c < x:
        r, c = r, c
    elif r < x:
        r, c = r, c - x
        ans += x ** 2
    elif c < x:
        r, c = r - x, c
        ans += 2 * x ** 2
    else:
        r, c = r - x, c - x
        ans += 3 * x ** 2
    N -= 1
print(ans)

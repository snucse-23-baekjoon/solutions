d, n = map(int, input().split())
x, y = map(int, input().split())
a = 0
tmp = n
row, col = 1, 1
while tmp:
    b = tmp % 10
    if b == 1:
        row = row
        col += 2 ** a
    elif b == 2:
        row = row
        col = col
    elif b == 3:
        row += 2 ** a
        col = col
    else:
        row += 2 ** a
        col += 2 ** a
    tmp = tmp // 10
    a += 1
row -= y
col += x
if 1 <= row <= 2 ** d and 1 <= col <= 2 ** d:
    ans = ''
    a = 2 ** (d - 1)
    for i in range(d):
        if row / a > 1 and col / a > 1:
            ans += '4'
            row -= a
            col -= a
        elif row / a > 1:
            ans += '3'
            row -= a
        elif col / a > 1:
            ans += '1'
            col -= a
        else:
            ans += '2'
        a = a // 2
    print(ans)
else:
    print(-1)

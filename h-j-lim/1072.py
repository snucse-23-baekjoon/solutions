X, Y = map(int, input().split())
Z = (100 * Y) // X
if Z >= 99:
    print(-1)
else:
    left = 0
    right = 1000000000
    while left + 1 < right:
        mid = (left + right) // 2
        Z_new = (100 * (Y + mid)) // (X + mid)
        if Z_new >= Z + 1:
            right = mid
        else:
            left = mid
    if (100 * (Y + left)) // (X + left) > Z:
        print(left)
    else:
        print(right)

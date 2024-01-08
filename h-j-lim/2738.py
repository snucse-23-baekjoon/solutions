row, col = 1, 1
M = 0
for i in range(9):
    a = list(map(int, input().split()))
    for j in range(9):
        if a[j] > M:
            row, col = i + 1, j + 1
            M = a[j]
print(M)
print(row, col)
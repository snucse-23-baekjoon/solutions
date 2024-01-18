def slope(a, b):
    return (heights[a] - heights[b]) / (a - b)


N = int(input())
heights = list(map(int, input().split()))
A = [0] * N
for i in range(1, N):  # left
    count = 0
    for j in range(i):
        tmp = slope(i, j)
        if all(list(map(lambda x: tmp - slope(i, x) < 0, range(j + 1, i)))):
            count += 1
    A[i] = count
for i in range(N - 1):  # right
    count = 0
    for j in range(i + 1, N):
        tmp = slope(i, j)
        if all(list(map(lambda x: tmp - slope(i, x) > 0, range(i + 1, j)))):
            count += 1
    A[i] += count
print(max(A))

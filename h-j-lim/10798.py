paper = [[0 for j in range(100)] for i in range(100)]
area = 0
N = int(input())
for i in range(N):
    x, y = map(int, input().split())
    for j in range(x, x + 10):
        for k in range(y, y + 10):
            paper[j][k] = 1
for i in range(100):
    for j in range(100):
        if paper[i][j]:
            area += 1
print(area)

N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

for i in range(N):
    scores[i] = scores[i] / M * 100

mean = sum(scores) / N
print(mean)

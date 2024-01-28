K = int(input())
L = []
for _ in range(6):
    x = tuple(map(int, input().split()))
    L.append(x)
L *= 2
i = 0
while i < 12:
    if L[i][0] == L[i + 2][0] and L[i + 1][0] == L[i + 3][0]:
        break
    i += 1
ans = K * (L[i + 4][1] * L[i + 5][1] - L[i + 1][1] * L[i + 2][1])
print(ans)

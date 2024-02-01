N, S, M = map(int, input().split())
V = list(map(int, input().split()))
DP = [S]
for i in range(N):
    tmp = []
    for num in DP:
        if num not in tmp:
            tmp.append(num)
    DP.clear()
    DP += list(filter(lambda x: x <= M, map(lambda x: x + V[i], tmp)))
    DP += list(filter(lambda x: x >= 0, map(lambda x: x - V[i], tmp)))
    tmp.clear()
    if not DP:
        break
if not DP:
    print(-1)
else:
    print(max(DP))

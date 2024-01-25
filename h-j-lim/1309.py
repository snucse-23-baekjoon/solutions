N = int(input())
DP = [1, 1, 1]
for _ in range(N - 1):
    tmp = DP[:]
    DP[0] = tmp[0] + tmp[1] + tmp[2]
    DP[1] = tmp[0] + tmp[2]
    DP[2] = tmp[0] + tmp[1]
print(sum(DP) % 9901)

import sys
sys.stdin = open("../input.txt", 'r')

M = 10_007
S = sys.stdin.readline().rstrip()
N = len(S)
dp = [[0] * N for _ in range(N)]

for i in range(N):
    for j in range(N - i):
        s, e = j, i + j
        if s == e:
            dp[s][e] = 1
        elif S[s] == S[e]:
            dp[s][e] = (dp[s][e - 1] + dp[s + 1][e] + 1) % M
        else:
            dp[s][e] = (dp[s][e - 1] + dp[s + 1][e] - dp[s + 1][e - 1]) % M

print(dp[0][-1])

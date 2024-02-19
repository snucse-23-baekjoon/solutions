import sys


N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
    coin = int(sys.stdin.readline())
    coins.append(coin)
i = N - 1
ans = 0
while K:
    num_coin = K // coins[i]
    K -= num_coin * coins[i]
    ans += num_coin
    i -= 1
print(ans)

memo = [0 for i in range(1000001)]


def to1(x):
    if x == 1:
        return 0
    if x % 3 == 0 and x % 2 == 0:
        memo[x] = to1(x // 6) + 2
        return memo[x]
    elif x % 3 == 0:
        memo[x] = min(to1(x // 3), to1(x - 1)) + 1
        return memo[x]
    elif x % 2 == 0:
        memo[x] = min(to1(x // 2), to1(x - 1)) + 1
        return memo[x]
    else:
        memo[x] = to1(x - 1) + 1
        return memo[x]


for i in range(1000000):
    print(to1(i))
N = int(input())
print(to1(N))

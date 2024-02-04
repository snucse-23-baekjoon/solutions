mod = 1000000000
n = int(input())
d = [[0]*(1024) for i in range(10)]
for i in range(10):
    d[i][1<<i] = 1
for i in range(2, n+1):
    tmp = [[0]*(1024) for i in range(10)]
    for j in range(10):
        for k in range(1024):
            if j > 0:
                tmp[j][k|(1<<j)] += d[j-1][k]
            if j < 9:
                tmp[j][k|(1<<j)] += d[j+1][k]
            tmp[j][k|(1<<j)] %= mod
    d = tmp
print(sum([d[i][1023] for i in range(1, 10)]) % mod)
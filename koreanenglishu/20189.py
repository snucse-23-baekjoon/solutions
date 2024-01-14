from sys import stdin
stdin = open("../input.txt", 'r')

N, K, Q = map(int, stdin.readline().split())
dist_sum = 0

for i in range(1, N + 1):
    for n in map(int, stdin.readline().split()):
        dist_sum += (n - i) % N
    if i == 1 and dist_sum == 0:
        dist_sum += N

print(int(dist_sum // N <= Q))

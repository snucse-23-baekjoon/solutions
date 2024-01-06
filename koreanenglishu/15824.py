import sys
sys.stdin = open("../input.txt", 'r')

M = 1_000_000_007
N = int(sys.stdin.readline())
arr = sorted(list(map(int, sys.stdin.readline().split())))

res = 0
aux = 2
for i in range(1, N):
    j = N - i - 1
    res = (res + (aux - 1) * (arr[i] - arr[j])) % M
    aux = (aux * 2) % M

print(res)

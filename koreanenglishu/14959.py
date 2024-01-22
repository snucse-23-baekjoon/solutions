from sys import stdin
stdin = open("../input.txt", 'r')

n = int(stdin.readline()); pi = [0] * n
arr = list(map(int, stdin.readline().split()))[::-1]

j = 0
for i in range(1, n):
    while j > 0 and arr[i] != arr[j]: j = pi[j - 1]
    if arr[i] == arr[j]: j += 1; pi[i] = j

ans_k, ans_p = 0, n
for i in range(n):
    k, p = n - i - 1, i - pi[i] + 1
    if (k + p, p) < (ans_k + ans_p, ans_p):
        ans_k, ans_p = k, p

print(ans_k, ans_p)

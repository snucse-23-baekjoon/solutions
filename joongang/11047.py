from sys import stdin
n, k = map(int, stdin.readline().split())
lst = [int(stdin.readline()) for i in range(n)]
ans = 0
s = 0
while s < k:
    ans += (k-s) // lst[n-1]
    s += (k-s) // lst[n-1] * lst[n-1]
    n -= 1
print(ans)
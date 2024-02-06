from sys import stdin
n, s = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
d = [0]
for i in range(n):
    d.append(d[i] + lst[i])
lp = 0
rp = 1
ans = 0
while lp < rp <= n:
    cand = d[rp] - d[lp]
    if cand >= s:
        if ans:
            ans = min(ans, rp-lp)
        else:
            ans = rp-lp
        lp += 1
    else:
        rp += 1
print(ans)
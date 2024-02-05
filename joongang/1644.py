from sys import stdin
n = int(stdin.readline())
if n==1:
    print(0)
    exit()
chk = [0 for i in range(n+1)]
prime = []
for i in range(2, n+1):
    if not chk[i]:
        prime.append(i)
        j = 1
        while i*j<=n:
            chk[i*j] = 1
            j += 1
l = len(prime)
s = [0]
for i in range(1, l+1):
    s.append(s[i-1] + prime[i-1])
p1 = 0
p2 = 1
ans = 0
while p1 < p2 <= l:
    svalue = s[p2]-s[p1]
    if svalue == n:
        ans += 1
        p1 += 1
        p2 += 1
    elif svalue > n:
        p1 += 1
    else:
        p2 += 1
print(ans)
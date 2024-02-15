from sys import stdin
t = int(stdin.readline())
n = int(stdin.readline())
lst1 = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
lst2 = list(map(int, stdin.readline().split()))
ans = 0
s1 = [0]
s2 = [0]
d = {}
for i in range(n):
    s1.append(s1[i]+lst1[i])
for i in range(n+1):
    for j in range(i+1, n+1):
        s = s1[j] - s1[i]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
for i in range(m):
    s2.append(s2[i]+lst2[i])
for i in range(m+1):
    for j in range(i+1, m+1):
        s = t - (s2[j] - s2[i])
        if s in d:
            ans += d[s]
print(ans)
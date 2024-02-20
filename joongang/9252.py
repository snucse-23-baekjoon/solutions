from sys import stdin
s1 = stdin.readline().rstrip()
s2 = stdin.readline().rstrip()
l1 = len(s1)
l2 = len(s2)
d = [['']*(l2+1) for i in range(l1+1)]
for i in range(1, l1+1):
    for j in range(1, l2+1):
        if s1[i-1] == s2[j-1]:
            d[i][j] = d[i-1][j-1] + s1[i-1]
        else:
            d[i][j] = d[i-1][j] if len(d[i-1][j])>len(d[i][j-1]) else d[i][j-1]
print(len(d[-1][-1]))
print(d[-1][-1])
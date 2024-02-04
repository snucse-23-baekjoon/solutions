s = input()
n = len(s)
table = [[0]*n for i in range(n)]
for i in range(n):
    table[i][i] = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        table[i][i+1] = 1
for i in range(2, n):
    for j in range(i-1):
        if s[i] == s[j] and table[j+1][i-1]:
            table[j][i] = 1
d = [0]*n
d[0] = 1
for i in range(1, n):
    m = d[i-1] + 1
    for j in range(i):
        if table[j][i]:
            m = min(m, d[j-1] + 1)
    d[i] = m
print(d[-1])
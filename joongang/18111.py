from sys import stdin
n, m, b = map(int, stdin.readline().split())
lst = []
for _ in range(n):
    lst.append(list(map(int, stdin.readline().split())))
t = 500**2 * 512
ans = 0
Maximum = lst[0][0]
minimum = lst[0][0]
s = sum(list(map(sum, lst)))
for i in range(n):
    for j in range(m):
        if lst[i][j] > Maximum:
            Maximum = lst[i][j]
        if lst[i][j] < minimum:
            minimum = lst[i][j]
for i in range(minimum, Maximum+1):
    if m*n*i <= s+b:
        tmp = 0
        for j in range(n):
            for k in range(m):
                if lst[j][k] > i:
                    tmp += 2*(lst[j][k]-i)
                elif lst[j][k] < i:
                    tmp += i - lst[j][k]
        if tmp <= t:
            t = tmp
            ans = i
print(t, ans)
m, n = map(int, input().split())
m = 2 if m == 1 else m
lst = [1 for i in range(n-1)]
i = 2
while i != n:
    j = 2
    while i * j <= n:
        lst[i*j-2] = 0
        j += 1
    i += 1
for i in range(m-2, n-1):
    if lst[i]:
        print(i+2)
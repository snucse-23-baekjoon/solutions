n = int(input())
L = [0, 1, 2]
i = 3
while i <= n:
    L.append(L[i - 1] + L[i - 2])
    i += 1
print(L[n] % 10007)

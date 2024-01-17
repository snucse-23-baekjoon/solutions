def xor(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result

from sys import stdin
t = int(stdin.readline())
for _ in range(t):
    n = int(stdin.readline())
    lst = stdin.readline().rstrip().split()
    ans = 8
    if n > 32:
        print(0)
        continue
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if i == j or j == k or k == i:
                    continue
                else:
                    dist = xor(lst[i], lst[j]) + xor(lst[j], lst[k]) + xor(lst[k], lst[i])
                    ans = min(ans, dist)
    print(ans)
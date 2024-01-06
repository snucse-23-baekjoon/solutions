from sys import stdin
n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
lst = list(filter(lambda x: x<m, lst))
ans = 0
for i in range(len(lst)):
    for j in range(len(lst)):
        for k in range(len(lst)):
            if i==j or i==k or j==k:
                continue
            s = lst[i]+lst[j]+lst[k]
            if s > m:
                continue
            if s > ans:
                ans = s
print(ans)
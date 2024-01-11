n, k = map(int, input().split())
lst = [i for i in range(1, n+1)]
ans = []
idx = 0
while lst:
    idx = idx + k - 1
    while idx >= len(lst):
        idx -= len(lst)
    ans.append(lst.pop(idx))
print('<', end='')
for i in range(n-1):
    print(f'{ans[i]}, ', end='')
print(f'{ans[-1]}>')

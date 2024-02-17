N, K = map(int, input().split())
lst = list(range(1, N + 1))
index = K - 1
res = []
for i in range(N):
    index %= len(lst)
    res.append(str(lst[index]))
    lst.pop(index)
    index += K - 1
ans = '<' + ', '.join(res) + '>'
print(ans)

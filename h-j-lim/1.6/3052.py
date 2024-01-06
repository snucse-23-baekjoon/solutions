N, M = map(int, input().split())
l = list(range(N + 1))
for i in range(M):
    a, b = map(int, input().split())
    l[a : b + 1] = reversed(l[a : b + 1])
l.remove(0)
print(*l)
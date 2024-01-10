from sys import stdin
n = int(stdin.readline())
lst = []
for _ in range(n):
    lst.append(list(map(int, stdin.readline().split())))
lst.sort(key = lambda x: (x[1], x[0]))
ans = 0
end = 0
for i in lst:
    if i[0] >= end:
        ans += 1
        end = i[1]
print(ans)
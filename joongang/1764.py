from sys import stdin
n, m = map(int, stdin.readline().split())
set1 = set()
set2 = set()
for _ in range(n):
    set1.add(stdin.readline().rstrip())
for _ in range(m):
    set2.add(stdin.readline().rstrip())
ans = []
for i in set1:
    if i in set2:
        ans.append(i)
ans.sort()
print(len(ans))
for i in ans:
    print(i)
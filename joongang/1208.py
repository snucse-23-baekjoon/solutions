from sys import stdin
from itertools import combinations
n, s = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
lst1 = lst[:len(lst)//2]
lst2 = lst[len(lst)//2:]
s1 = []
s2 = []
for i in range(len(lst1)+1):
    for j in combinations(lst1, i):
        s1.append(sum(j))
for i in range(len(lst2)+1):
    for j in combinations(lst2, i):
        s2.append(sum(j))
s1.sort()
s2.sort(reverse=1)
ans = 0
p1 = 0
p2 = 0
l1 = len(s1)
l2 = len(s2)
while p1 < l1 and p2 < l2:
    sprime = s1[p1] + s2[p2]
    if sprime == s:
        tmp1, tmp2 = p1, p2
        while tmp1 < l1 and s1[tmp1] == s1[p1]:
            tmp1 += 1
        while tmp2 < l2 and s2[tmp2] == s2[p2]:
            tmp2 += 1
        ans += (tmp1 - p1) * (tmp2 - p2)
        p1, p2 = tmp1, tmp2
    elif sprime > s:
        p2 += 1
    else:
        p1 += 1
if s == 0:
    ans -= 1
print(ans)
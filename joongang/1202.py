from sys import stdin
import heapq
n, k = map(int, stdin.readline().split())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
chk = [0]*n
bag = [int(stdin.readline()) for i in range(k)]
bag.sort()
lst.sort()
q = []
ans = 0
for i in bag:
    while lst and lst[0][0] <= i:
        heapq.heappush(q, -lst[0][1])
        heapq.heappop(lst)
    if q:
        ans -= heapq.heappop(q)
print(ans)
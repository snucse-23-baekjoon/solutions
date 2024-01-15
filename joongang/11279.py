from sys import stdin
import heapq
n = int(stdin.readline())
heap = []
for _ in range(n):
    x = int(stdin.readline())
    if x:
        heapq.heappush(heap, -x)
    elif heap:
        print(-heapq.heappop(heap))
    else:
        print(0)
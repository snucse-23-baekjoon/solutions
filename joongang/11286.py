from sys import stdin
import heapq
n = int(stdin.readline())
heap = []
d = dict()
for _ in range(n):
    x = int(stdin.readline())
    if x:
        heapq.heappush(heap, abs(x))
        if x in d:
            d[x] += 1
        else:
            d[x] = 1
    elif heap:
        num = heapq.heappop(heap)
        if -num in d:
            print(-num)
            d[-num] -= 1
            if d[-num] == 0:
                del d[-num]
        else:
            print(num)
            d[num] -= 1
            if d[num] == 0:
                del d[num]
    else:
        print(0)
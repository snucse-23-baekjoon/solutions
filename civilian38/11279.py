import sys
from heapq import heappush, heappop

heap = list()
repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    operation = int(sys.stdin.readline().rstrip())
    if operation:
        heappush(heap, (- operation, operation))
    else:
        if heap:
            print(heappop(heap)[1])
        else:
            print(0)
def empty(nums):
    for i in nums:
        if nums[i] > 0:
            return 0
    return 1

from sys import stdin
import heapq
t = int(stdin.readline())
for _ in range(t):
    k = int(stdin.readline())
    minh = []
    maxh = []
    nums = dict()
    for __ in range(k):
        op = stdin.readline().rstrip()
        if op[0] == 'I':
            n = int(op[2:])
            if n in nums:
                nums[n] += 1
            else:
                nums[n] = 1
                heapq.heappush(minh, n)
                heapq.heappush(maxh, -n)
            
        elif not empty(nums):
            if op[2] == '1':
                while -maxh[0] not in nums or nums[-maxh[0]] < 1:
                    tmp = -heapq.heappop(maxh)
                    if tmp in nums:
                        del(nums[tmp])
                nums[-maxh[0]] -= 1
            else:
                while minh[0] not in nums or nums[minh[0]] < 1:
                    tmp = heapq.heappop(minh)
                    if tmp in nums:
                        del(nums[tmp])
                nums[minh[0]] -= 1
    if not empty(nums):
        while minh[0] not in nums or nums[minh[0]] < 1:
            heapq.heappop(minh)
        while -maxh[0] not in nums or nums[-maxh[0]] < 1:
            heapq.heappop(maxh)
        print(-maxh[0], minh[0])
    else:
        print('EMPTY')
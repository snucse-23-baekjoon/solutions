import sys


N = int(sys.stdin.readline())
min_heap = [0]
len_heap = 0
for _ in range(N):
    a = int(sys.stdin.readline())
    if a:
        len_heap += 1
        min_heap.append(a)
        tmp = len_heap
        while min_heap[tmp] < min_heap[tmp // 2]:
            min_heap[tmp], min_heap[tmp // 2] = min_heap[tmp // 2], min_heap[tmp]
            tmp = tmp // 2
    else:
        if len_heap == 0:
            print(0)
        elif len_heap == 1:
            print(min_heap.pop())
            len_heap -= 1
        else:
            min_heap[len_heap], min_heap[1] = min_heap[1], min_heap[len_heap]
            print(min_heap.pop())
            len_heap -= 1
            if len_heap == 1:
                continue
            elif len_heap == 2:
                if min_heap[1] > min_heap[2]:
                    min_heap[1], min_heap[2] = min_heap[2], min_heap[1]
            else:
                tmp = 1
                to_comp = 2 if min_heap[2] < min_heap[3] else 3
                while tmp * 2 <= len_heap and min_heap[tmp] > min_heap[to_comp]:
                    min_heap[tmp], min_heap[to_comp] = min_heap[to_comp], min_heap[tmp]
                    tmp = to_comp
                    if tmp * 2 + 1 <= len_heap:
                        to_comp = 2 * tmp if min_heap[2 * tmp] < min_heap[2 * tmp + 1] else 2 * tmp + 1
                    else:
                        to_comp = tmp * 2

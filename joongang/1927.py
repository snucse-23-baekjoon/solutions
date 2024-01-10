from sys import stdin
n = int(stdin.readline())
heap = [0 for i in range(200010)]
size = 0
for _ in range(n):
    operand = int(stdin.readline())
    if operand:
        size += 1
        heap[size] = operand
        i = 0
        while heap[size//(2**i)] < heap[size//(2**(i+1))]:
            heap[size//(2**i)], heap[size//(2**(i+1))] = heap[size//(2**(i+1))], heap[size//(2**i)]
            i += 1
    else:
        print(heap[1])
        heap[1] = heap[size]
        heap[size] = 0
        size = max(0, size-1)
        i = 1
        while min(heap[i*2], heap[i*2+1]) < heap[i] and (heap[i*2] or heap[i*2+1]):
            if heap[i*2] <= heap[i*2+1] and heap[i*2]:
                heap[i], heap[i*2] = heap[i*2], heap[i]
                i = i*2
            elif heap[i*2] > heap[i*2+1] and heap[i*2+1]:
                heap[i], heap[i*2+1] = heap[i*2+1], heap[i]
                i = i*2 + 1
            elif heap[i] > heap[i*2] > 0:
                heap[i], heap[i*2] = heap[i*2], heap[i]
                i = i*2
            elif heap[i] > heap[i*2+1] > 0:
                heap[i], heap[i*2+1] = heap[i*2+1], heap[i]
                i = i*2 + 1
            else:
                break
def distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

import sys
sys.stdin = open('case4.txt')

size, number = tuple(map(int, sys.stdin.readline().split()))
queue = [i for i in range(1, 1 + size)]
target = [int(i) for i in sys.stdin.readline().split()]

count = 0
while target:
    if queue[0] == target[0]:
        queue.pop(0)
        target.pop(0)
    else:
        if len(queue) - queue.index(target[0]) < queue.index(target[0]):
            count += len(queue) - queue.index(target[0])
            
        else:
            count += queue.index(target[0])
        queue = queue[queue.index(target[0]):] + queue[:queue.index(target[0])]
print(count)
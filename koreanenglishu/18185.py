from sys import stdin
stdin = open("../input.txt", 'r')

n = int(stdin.readline())
queue = []
ramen = 0
box = 0

for a in map(int, stdin.readline().split()):
    ramen += a
    if len(queue) - a > 0:
        box += len(queue) - a
        queue = queue[len(queue) - a:]

    i = 0
    while i < len(queue) and queue[i] == 3:
        i += 1
    box += i
    queue = queue[i:]

    for i in range(a):
        if i < len(queue):
            queue[i] += 1
        else:
            queue.append(1)

box += len(queue)
print(ramen * 2 + box)

from sys import stdin
n = int(stdin.readline())
queue = []
for _ in range(n):
    opcode = stdin.readline().split()
    if opcode[0] == 'push':
        queue.append(int(opcode[1]))
    elif opcode[0] == 'pop':
        if queue:
            print(queue[0])
            queue.pop(0)
        else:
            print(-1)
    elif opcode[0] == 'size':
        print(len(queue))
    elif opcode[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif opcode[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif opcode[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)
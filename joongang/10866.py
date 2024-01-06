from sys import stdin
n = int(stdin.readline())
deque = []
for _ in range(n):
    opcode = stdin.readline().split()
    if opcode[0] == 'push_front':
        deque = [int(opcode[1])] + deque
    elif opcode[0] == 'push_back':
        deque.append(int(opcode[1]))
    elif opcode[0] == 'pop_front':
        if deque:
            print(deque[0])
            deque.pop(0)
        else:
            print(-1)
    elif opcode[0] == 'pop_back':
        if deque:
            print(deque[-1])
            deque.pop()
        else:
            print(-1)
    elif opcode[0] == 'size':
        print(len(deque))
    elif opcode[0] == 'empty':
        if deque:
            print(0)
        else:
            print(1)
    elif opcode[0] == 'front':
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif opcode[0] == 'back':
        if deque:
            print(deque[-1])
        else:
            print(-1)
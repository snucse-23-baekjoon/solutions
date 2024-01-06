from sys import stdin
n = int(stdin.readline())
stack = []
for _ in range(n):
    opcode = stdin.readline().split()
    if opcode[0] == 'push':
        stack.append(int(opcode[1]))
    elif opcode[0] == 'pop':
        if stack:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)
    elif opcode[0] == 'size':
        print(len(stack))
    elif opcode[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)
    elif opcode[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
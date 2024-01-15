from sys import stdin
m = int(stdin.readline())
S = set()
for _ in range(m):
    op = stdin.readline().rstrip().split()
    opcode = op[0]
    if len(op) > 1:
        operand = int(op[1])
    if opcode == 'add':
        S.add(operand)
    elif opcode == 'remove':
        S.discard(operand)
    elif opcode == 'check':
        if operand in S:
            print(1)
        else:
            print(0)
    elif opcode == 'toggle':
        if operand in S:
            S.remove(operand)
        else:
            S.add(operand)
    elif opcode == 'all':
        S = {i for i in range(1, 21)}
    elif opcode == 'empty':
        S = set()
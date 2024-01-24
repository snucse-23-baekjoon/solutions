import sys
sys.stdin = open('case2.txt')

number = int(sys.stdin.readline().rstrip())
output = list(map(int, [sys.stdin.readline().rstrip() for _ in range(number)]))
stack = list()
history = list()
left = [i for i in range(1, 1 + number)]

while left or stack:
    if stack:
        if output[0] > stack[-1]:
            stack.append(left.pop(0))
            history.append('+')
        elif output[0] == stack[-1]:
            output.pop(0)
            stack.pop(-1)
            history.append('-')
        else:
            history = list()
            break
    else:
        stack.append(left.pop(0))
        history.append('+')

if history:
    any(map(print, history))
else:
    print('NO')
from sys import stdin
s = stdin.readline().rstrip()
target = list(stdin.readline().rstrip())
l = len(target)
stack = []
for i in s:
    stack.append(i)
    if stack[-l:] == target:
        for j in range(l):
            stack.pop()
if stack:
    print(''.join(stack))
else:
    print('FRULA')
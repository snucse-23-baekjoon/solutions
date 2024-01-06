from sys import stdin
while 1:
    t = stdin.readline().rstrip()
    if t == '.':
        break
    stack = []
    chk = 0
    for i in t:
        if i == '(' or i == '[':
            stack.append(i)
        if i == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                print('no')
                chk = 1
                break
        if i == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                print('no')
                chk = 1
                break
    if not chk:
        if not stack:
            print('yes')
        else:
            print('no')
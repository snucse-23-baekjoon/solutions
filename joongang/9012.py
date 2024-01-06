from sys import stdin
t = int(stdin.readline())
for i in range(t):
    s = stdin.readline().strip()
    stack = []
    chk = 0
    for j in s:
        if j == '(':
            stack.append('(')
        elif j == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                chk = 1
                break
    if stack:
        chk = 1
    if chk:
        print('NO')
    else:
        print('YES')
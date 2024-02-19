import sys


n = int(sys.stdin.readline())
stack, res = [], []
flag = True
i = 1
for _ in range(n):
    x = int(sys.stdin.readline())
    if i <= x:
        while i <= x:
            stack.append(i)
            res.append('+')
            i += 1
        stack.pop()
        res.append('-')
    else:
        if stack and stack[-1] >= x:
            while stack and stack[-1] >= x:
                stack.pop()
                res.append('-')
        else:
            flag = False
if flag:
    for op in res:
        print(op)
else:
    print('NO')

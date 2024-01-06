from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    lst.append(int(stdin.readline()))
stack = [1]
ans = ['+']
pushnum = 2
while lst:
    if not stack or lst[0] > stack[-1]:
        ans.append('+')
        stack.append(pushnum)
        pushnum += 1
    elif lst[0] == stack[-1]:
        ans.append('-')
        lst.pop(0)
        stack.pop()
    else:
        break
if not lst:
    for i in ans:
        print(i)
else:
    print('NO')
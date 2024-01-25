s = input()
pm = ['+', '-']
md = ['*', '/']
stack = []
ans = ''
for i in range(len(s)):
    tmp = s[i]
    if tmp.isalpha():
        ans += s[i]
    elif tmp == '(':
        stack.append(tmp)
    elif tmp == ')':
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.pop()
    elif tmp in pm:
        while stack and stack[-1] != '(':
            ans += stack.pop()
        stack.append(tmp)
    elif tmp in md:
        while stack and stack[-1] in md:
            ans += stack.pop()
        stack.append(tmp)
while stack:
    ans += stack.pop()
print(ans)
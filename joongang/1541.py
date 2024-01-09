s = input()
lst = []
num = ''
for i in s:
    if i == '+' or i == '-':
        lst.append(num)
        lst.append(i)
        num = ''
    else:
        num += i
lst.append(num)
lst = list(map(lambda x: x if x == '+' or x == '-' else int(x), lst))
ans = 0
sign = 1
for i in lst:
    if i == '-':
        if sign == 1:
            sign *= -1
    elif i == '+':
        continue
    else:
        ans += i*sign
print(ans)
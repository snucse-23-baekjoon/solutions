s = input().split('-')
for i in range(len(s)):
    x = s[i].split('+')
    for j in range(len(x)):
        x[j].lstrip('0')
        x[j] = int(x[j])
    s[i] = sum(x)
if len(s) == 1:
    print(*s)
else:
    print(s[0] - sum(s[1:]))

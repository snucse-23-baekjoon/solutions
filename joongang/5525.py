from sys import stdin
n = int(stdin.readline())
m = int(stdin.readline())
s = stdin.readline().rstrip()
cnt = 0
ans = 0
for i in range(m-1):
    if s[i] == 'I':
        if s[i+1] == 'I':
            cnt = 0
    else:
        if i and s[i-1] == 'I' and s[i+1] == 'I':
            cnt += 1
        else:
            cnt = 0
    if cnt == n:
        ans += 1
        cnt -= 1
print(ans)
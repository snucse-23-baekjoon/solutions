from sys import stdin
x = int(stdin.readline())
n = int(stdin.readline())
s = 0
for i in range(n):
    a, b = map(int, stdin.readline().split())
    s += a*b
if s==x:
    print('Yes')
else:
    print('No')
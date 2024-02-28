from sys import stdin
t = int(stdin.readline())
for i in range(1, t+1):
    a, b = map(int, stdin.readline().split())
    print(f'Case #{i}: {a} + {b} = {a+b}')
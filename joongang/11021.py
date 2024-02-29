from sys import stdin
t = int(stdin.readline())
for i in range(1, t+1):
    print(f'Case #{i}: {sum(map(int, stdin.readline().split()))}')
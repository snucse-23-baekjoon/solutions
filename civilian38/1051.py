import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
square = [[int(number) for number in line] for line in [sys.stdin.readline().rstrip() for _ in range(n)]]
if n > m:
    square = list(zip(*square))

keep = True
for i in range(min(n, m) - 1, -1, -1):
    for j in range(min(n, m) - i):
        for k in range(max(n, m) - i):
            if square[j][k] == square[j + i][k] == square[j][k + i] == square[j + i][k + i]:
                if keep:
                    print((i+1)**2)
                    keep = False
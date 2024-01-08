import sys

x,y = tuple(map(int,sys.stdin.readline().split()))
grid = [sys.stdin.readline().rstrip() for _ in range(x)]

fst = 0
for line in grid:
    if "X" not in line:
        fst += 1

snd = 0
for line in zip(*grid):
    if "X" not in line:
        snd += 1

print(max((fst,snd)))
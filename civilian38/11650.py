import sys

repeat = int(sys.stdin.readline().rstrip())
data = [list(map(int, sys.stdin.readline().split())) for _ in range(repeat)]
data.sort()

for datum in data:
    print(*datum)
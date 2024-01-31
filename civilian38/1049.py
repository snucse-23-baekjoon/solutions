import sys

strings, repeat = tuple(map(int,sys.stdin.readline().split()))

data = list(zip(*[list(map(int, sys.stdin.readline().split())) for _ in range(repeat)]))
sets = min(data[0])
single = min(data[1])

if sets > single * 6:
    print(strings * single)
else:
    print(min(((strings // 6) * sets + (strings % 6) * single, sets * ((strings // 6) + 1))))
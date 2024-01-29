import sys

a, b, c = tuple(sorted(map(int, sys.stdin.readline().split())))
while a or b or c:
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')
    a, b, c = tuple(sorted(map(int, sys.stdin.readline().split())))   
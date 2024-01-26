import sys

length = int(sys.stdin.readline().rstrip())
data = set()
any(map(lambda x: data.add(int(x)), sys.stdin.readline().split()))

repeat = int(sys.stdin.readline().rstrip())
for i in tuple(map(int, sys.stdin.readline().split())):
    if i in data:
        print(1)
    else:
        print(0)
import sys

count = 1
repeat = int(sys.stdin.readline().rstrip())

while(repeat):
    names = dict()
    for i in range(1, 1 +repeat):
        names[i] = sys.stdin.readline().rstrip()
    storage = [0] * repeat
    for _ in range(repeat * 2 - 1):
        storage[int(sys.stdin.readline().split()[0]) - 1] += 1
    print(count, names[storage.index(1) + 1])
    count += 1
    repeat = int(sys.stdin.readline().rstrip())
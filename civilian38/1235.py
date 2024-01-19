import sys

repeat = int(sys.stdin.readline().rstrip())
arrs = [sys.stdin.readline().rstrip() for _ in range(repeat)]

if len(arrs[0]) == 1:
    print(1)
else:
    for i in range(1, len(arrs[0]) + 1):
        data = set()
        for j in range(repeat):
            data.add(arrs[j][len(arrs[0]) - i:])
        if len(arrs) == len(data):
            print(i)
            break
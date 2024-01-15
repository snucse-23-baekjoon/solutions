import sys


n = int(input())
for i in range(n):
    inf = list(map(int, sys.stdin.readline().split()))
    half = inf.pop(0) // 2
    D = {}
    for army in inf:
        if army not in D:
            D[army] = 1
        else:
            D[army] += 1
    x = -1
    for army in D:
        if D[army] > half:
            x = army
    if x != -1:
        print(x)
    else:
        print('SYJKGW')

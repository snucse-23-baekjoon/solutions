D = {}
N = int(input())
L1 = list(map(int, input().split()))
for x in L1:
    if x not in D:
        D[x] = 1
    else:
        D[x] += 1
M = int(input())
L2 = list(map(int, input().split()))
for x in L2:
    if x not in D:
        print(0, end=' ')
    else:
        print(D[x], end=' ')

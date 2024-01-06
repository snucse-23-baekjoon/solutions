from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
m = int(stdin.readline())
targets = list(map(int, stdin.readline().split()))
lst.sort()

for i in range(m):
    first = 0
    last = n-1
    chk = 0
    while first <= last:
        mid = (first + last) // 2
        if targets[i] == lst[mid]:
            print(1)
            chk = 1
            break
        elif targets[i] > lst[mid]:
            first = mid + 1
        else:
            last = mid - 1
    if not chk:
        print(0)
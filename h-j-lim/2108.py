import sys


N = int(input())
L = []
for i in range(N):
    L.append(int(sys.stdin.readline()))
L.sort()
D = {}
for num in L:
    if num not in D:
        D[num] = 1
    else:
        D[num] += 1
set_mode = set()
m = 0
for num in D:
    if D[num] > m:
        m = D[num]
        set_mode.clear()
        set_mode.add(num)
    if D[num] == m:
        set_mode.add(num)
list_mode = list(set_mode)
list_mode.sort()
mean = (round(sum(L) / len(L)))
median = L[N // 2]
mode = list_mode[1] if len(list_mode) >= 2 else list_mode[0]
Range = L[N - 1] - L[0]
print(mean)
print(median)
print(mode)
print(Range)


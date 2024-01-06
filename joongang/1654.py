from sys import stdin
k, n = list(map(int, stdin.readline().split()))
lst = []
for i in range(k):
    lst.append(int(stdin.readline()))
first = 1
last = sum(lst) // n
while last - first > 1:
    mid = (first + last) // 2
    tmp = sum(list(map(lambda x: x//mid, lst)))
    if tmp < n:
        last = mid
    else:
        first = mid
if sum(list(map(lambda x: x//last, lst))) >= n:
    print(last)
else:
    print(first)
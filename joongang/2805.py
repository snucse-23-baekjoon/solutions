from sys import stdin
n, m = map(int, stdin.readline().split())
lst = list(map(int, stdin.readline().split()))
top = max(lst)
bottom = 1
while bottom <= top:
    mid = (top + bottom) // 2
    s = 0
    for i in lst:
        if i > mid:
            s += i - mid
    if s >= m:
        bottom = mid + 1
    else:
        top = mid - 1
print(top)
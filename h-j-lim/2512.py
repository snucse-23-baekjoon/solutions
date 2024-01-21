N = int(input())
L = list(map(int, input().split()))
L.sort()
M = int(input())
if sum(L) <= M:
    print(max(L))
elif min(L) * N >= M:
    print(M // N)
else:
    i = N
    s = sum(L)
    while s > M:
        i -= 1
        s = sum(L[:i]) + (N - i) * L[i]
    left, right = L[i], L[i + 1]
    mid = (left + right) // 2
    while left < right - 1:
        s = sum(L[:i + 1]) + (N - i - 1) * mid
        if s == M:
            break
        elif s > M:
            right = mid
            mid = (left + right) // 2
        else:
            left = mid
            mid = (left + right) // 2
    print(mid)

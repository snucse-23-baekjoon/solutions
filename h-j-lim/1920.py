def binary_search(n, lst, left, right):
    if left == right:
        return False
    mid = (left + right) // 2
    if n == lst[mid]:
        return True
    elif n < lst[mid]:
        return binary_search(n, lst, left, mid)
    else:
        return binary_search(n, lst, mid + 1, right)


N = int(input())
L1 = list(map(int, input().split()))
M = int(input())
L2 = list(map(int, input().split()))
L1.sort()
for num in L2:
    if binary_search(num, L1, 0, N):
        print(1)
    else:
        print(0)

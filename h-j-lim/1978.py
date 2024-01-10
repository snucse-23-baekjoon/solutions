def prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for a in range(2, x // 2 + 1):
        if x % a == 0:
            return False
    return True


M = int(input())
N = int(input())
lst = []
for y in range(M, N + 1):
    if prime(y):
        lst.append(y)
if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)


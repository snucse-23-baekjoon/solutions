N = int(input())
lst = list(map(int, input().split()))
C = 0
for x in lst:
    if x == 1:
        C += 1
    else:
        for i in range(2, x // 2 + 1):
            if x % i == 0:
                C += 1
                break
print(N - C)

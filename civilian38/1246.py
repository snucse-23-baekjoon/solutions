import sys

n, m = tuple(map(int, sys.stdin.readline().split()))
arr = list(sorted([int(sys.stdin.readline().rstrip()) for _ in range(m)]))
maxprice = arr[0]
maxincome = maxprice * min((n, len(list(filter(lambda x: x >= maxprice, arr)))))

for i in range(1, m):
    if arr[i] * min((n, len(list(filter(lambda x: x >= arr[i], arr))))) > maxincome:
        maxprice = arr[i]
        maxincome = maxprice * min((n, len(list(filter(lambda x: x >= maxprice, arr)))))
print(maxprice, maxincome)
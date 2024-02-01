n, k = map(int, input().split())
arr = list(range(1, 1 + n))
count = 0;
print(end='<')
while len(arr) > 1:
    count = (count + k - 1) % len(arr)
    print(arr.pop(count), end = ', ')
print(arr[0], end='>')
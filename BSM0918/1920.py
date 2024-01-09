def binary_search(target, data):
    start = 0
    end = n-1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return True
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

        return False

n = int(input())
list_n = sorted(list(map(int, input().split())))

m = int(input())
list_m = list(map(int, input().split()))

for i in list_m:
    if binary_search(i, list_n):
        print(1)
    else:
        print(0)
            
    

def swap(arr, num1, num2):
    id1 = arr.index(num1)
    id2 = arr.index(num2)
    arr[id1] = num2
    arr[id2] = num1

repeat = int(input())
arr = [1,2,3]

for _ in range(repeat):
    target1, target2 = tuple(map(int, input().split()))
    swap(arr, target1, target2)
    
print(arr[0])
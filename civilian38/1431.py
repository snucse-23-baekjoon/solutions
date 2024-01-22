def convert(arr, first):
    if len(arr[first]) > len(arr[first + 1]):
        arr[first], arr[first + 1] = arr[first + 1], arr[first]
    elif len(arr[first]) == len(arr[first + 1]):
        first_num = sum(map(int, filter(lambda x: x in [str(i) for i in range(10)], arr[first])))
        second_num = sum(map(int, filter(lambda x: x in [str(i) for i in range(10)], arr[first + 1])))
        if second_num < first_num:
            arr[first], arr[first + 1] = arr[first + 1], arr[first]
        elif second_num == first_num:
            if arr[first] > arr[first + 1]:
                arr[first], arr[first + 1] = arr[first + 1], arr[first]
import sys

repeat = int(sys.stdin.readline().rstrip())
arr = [sys.stdin.readline().rstrip() for _ in range(repeat)]

for i in range(len(arr)):
    for j in range(len(arr) - i - 1):
        convert(arr, j)
        
any(map(print, arr))
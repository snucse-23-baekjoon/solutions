import sys

length = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().split()))
answer = [0] * length

for i in range(length):
    answer[arr.index(min(arr))] =  i
    arr[arr.index(min(arr))] = max(arr) + 1

for i in answer:
    print(i, end = ' ')
import sys

repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    number = int(sys.stdin.readline().rstrip())
    arr = [1,1,1]
    count = 3
    if number <= count:
        print(1)
    else:
        while count < number:
            count += 1
            arr = [arr[1], arr[2], arr[0] + arr[1]]
        print(arr[2])
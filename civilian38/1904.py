number = int(input()) + 1

count = 2
arr = [1, 1]

if number == 1 or number == 2:
    print(1)
else:
    while count < number:
        arr = [arr[1], sum(arr) % 15746]
        count += 1
    print(arr[-1])
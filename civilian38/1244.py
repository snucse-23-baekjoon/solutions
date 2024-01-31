import sys

numbers = int(sys.stdin.readline().rstrip())
switch = list(map(int, sys.stdin.readline().split()))
repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    gender, number = tuple(map(int, sys.stdin.readline().split()))
    index = number - 1
    if gender == 1:
        while index < numbers:
            switch[index] = 1 - switch[index]
            index += number
    else:
        switch[index] = 1 - switch[index]
        up = index + 1
        down = index - 1
        while down >= 0 and up < numbers and switch[up] == switch[down]:
            switch[up] = 1 - switch[up]
            switch[down] = 1 - switch[down]
            up += 1
            down -= 1

printed = 0
while switch:
    print(switch.pop(0), end='')
    printed += 1
    if printed % 20:
        print(end=' ')
    else:
        print()
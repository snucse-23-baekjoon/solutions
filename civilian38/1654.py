def whole(arr, length):
    return sum(map(lambda x: x // length, arr))

import sys
sys.stdin = open('case4.txt')

number, target = tuple(map(int, sys.stdin.readline().split()))
lines = tuple(map(int, [sys.stdin.readline().rstrip() for _ in range(number)]))

low, high = 1, max(lines)
while low < high:
    pin = (low + high) // 2
    if whole(lines, pin) < target:
        high = pin
    else:
        if low + 1 == high:
            if whole(lines, high) >= target:
                low = high
            else:
                high = low
        else:
            if whole(lines, pin) >= target:
                low = pin

print(low)
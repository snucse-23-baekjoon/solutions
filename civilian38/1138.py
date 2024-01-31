import sys

number = int(sys.stdin.readline().rstrip())
note = list(map(int, sys.stdin.readline().split()))
line = [0] * number

for i in range(number):
    index = 0
    count = 0
    while count < note[i]:
        if line[index] == 0:
            count += 1
        index += 1
    while line[index]:
        index += 1
    line[index] = i + 1

print(*line)
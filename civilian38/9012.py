import sys

number = int(sys.stdin.readline().rstrip())
for _ in range(number):
    data = sys.stdin.readline().rstrip()
    while '(' in data and ')' in data:
        if data[-1] == '(':
            break
        index = data.rindex('(')
        if index + 1 < len(data):
            data = data[:index] + data[index + 2:]
    if not data:
        print('YES')
    else:
        print('NO')
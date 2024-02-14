import sys

n = int(sys.stdin.readline().rstrip())
m = int(sys.stdin.readline().rstrip())
string = sys.stdin.readline().rstrip()

line = list()
while string:
    letter = string[0]
    string = string[1:]
    if letter == 'I':
        if line:
            if line[-1][-1] == "O":
                line[-1] = line[-1] + "I"
            else:
                line.append(letter)
        else:
            line.append(letter)
    else:
        if line and line[-1][-1] == "I":
            line[-1] = line[-1] + "O"
        else:
            line.append('O')
print(sum(map(lambda x: (len(x) // 2) - n + 1, filter(lambda x: len(x) >= 1 + (2 * n) and x[-1] == 'I', map(lambda x: x.strip('O'), line)))))
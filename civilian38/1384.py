import sys

repeat = int(sys.stdin.readline().rstrip())
count = 0

while repeat:
    count += 1
    print("Group", count)
    names = []
    letters = []
    for _ in range(repeat):
        data = sys.stdin.readline().split()
        names.append(data[0])
        letters.append(data[1:])
    for i in range(repeat):
        for j in range(repeat - 1):
            if letters[i][j] == 'N':
                print(names[(i - j - 1) % repeat], "was nasty about", names[i])
    if not any(map(lambda x : 'N' in x, letters)):
        print("Nobody was nasty")
    print()
    repeat = int(sys.stdin.readline().rstrip())
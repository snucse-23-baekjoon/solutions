import sys

repeatnum = int(sys.stdin.readline().rstrip())
data = [list(map(int,sys.stdin.readline().split())) for _ in range(repeatnum)]

accompany = [set() for _ in range(repeatnum)]
for grade in zip(*data):
    for single_student in range(repeatnum):
        for i in range(repeatnum):
            if grade[single_student] == grade[i]:
                accompany[single_student].add(i)

max_index = 0
for i in range(1,repeatnum):
    if len(accompany[i]) > len(accompany[max_index]):
        max_index = i
print(max_index + 1)
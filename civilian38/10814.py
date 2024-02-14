import sys

repeat = int(sys.stdin.readline().rstrip())
members = list()

for i in range(repeat):
    members.append([0,0,0])
    a, b = sys.stdin.readline().split()
    members[-1][0], members[-1][1], members[-1][2] = int(a), i, b

members.sort()
for i in range(repeat):
    age, index, name = tuple(members[i])
    print(age, name)
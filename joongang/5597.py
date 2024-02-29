from sys import stdin
lst = [0]*31
for i in range(28):
    lst[int(stdin.readline())] = 1
for i in range(1, 31):
    if not lst[i]:
        print(i)
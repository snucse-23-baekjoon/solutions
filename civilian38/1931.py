import sys

repeat = int(sys.stdin.readline().rstrip())
times = list()

for _ in range(repeat):
    times.append(tuple(map(int, sys.stdin.readline().split())))
times.sort(key=lambda x: (x[1], x[0]))

end = times[0][1]
count = 1
index = 1
while index < len(times):
    if times[index][0] >= end:
        end = times[index][1]
        count += 1
    index += 1

print(count)
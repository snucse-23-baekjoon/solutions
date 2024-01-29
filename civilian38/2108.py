import sys

number = int(sys.stdin.readline().rstrip())
data = list()
frequency = dict()
for _ in range(number):
    num = int(sys.stdin.readline().rstrip())
    data.append(num)
    if frequency.get(num):
        frequency[num] += 1
    else:
        frequency[num] = 1
data.sort()

print(round(sum(data)/number))
print(data[number//2])


max_frq = max(frequency.values())
rank = [k for k, v in frequency.items() if v == max_frq]
rank.sort()

if len(rank) > 1:
    print(rank[1])
else:
    print(rank[0])
print(max(data) - min(data))
N = int(input())
data = []

for i in range(N):
    value = input()
    data.append(value)

data = list(set(data))
data.sort()
data = sorted(data, key = len)

for x in data:
    print(x)

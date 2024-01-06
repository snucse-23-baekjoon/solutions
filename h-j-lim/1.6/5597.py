l = [0 for i in range(42)]
count = 0
for i in range(10):
    a = int(input())
    l[a % 42] = 1
for i in range(42):
    if l[i]:
        count += 1
print(count)
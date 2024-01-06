n = int(input())
targets = list(map(int, input().split()))
lst = [1 for i in range(999)]
i = 2
while i <= 32:
    j = 2
    while i * j <= 1000:
        lst[i*j-2] = 0
        j += 1
    i += 1
cnt = 0
for target in targets:
    if not target == 1 and lst[target-2]:
        cnt += 1
print(cnt)
from sys import stdin
n = int(stdin.readline())
lst = []
for i in range(n):
    lst.append(int(stdin.readline()))
lst.sort()
print(round(sum(lst)/n))
print(lst[n//2])
d = dict()
nums = list(set(lst))
for num in nums:
    d[num] = 0
for i in lst:
    d[i] += 1
maxvalue = max(d.values())
candidates = []
for num in nums:
    if d[num] == maxvalue:
        candidates.append(num)
candidates.sort()
print(candidates[0] if len(candidates) == 1 else candidates[1])
print(lst[-1]-lst[0])
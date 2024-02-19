import sys


n = int(sys.stdin.readline())
sum_1 = [int(sys.stdin.readline())]
for i in range(2, n + 1):
    tmp = list(map(int, sys.stdin.readline().split()))
    sum_2 = [sum_1[0] + tmp[0]]
    for j in range(1, i - 1):
        sum_2.append(max(sum_1[j - 1], sum_1[j]) + tmp[j])
    sum_2.append(sum_1[i - 2] + tmp[i - 1])
    sum_1 = sum_2[:]
print(max(sum_1))

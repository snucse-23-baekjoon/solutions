import sys


L = [1] * 10001
for num in range(2, 101):
    if L[num]:
        L[2 * num::num] = [0] * (10000 // num - 1)
T = int(input())
for _ in range(T):
    n = int(sys.stdin.readline())
    left, right = n // 2, n // 2
    while not L[left] or not L[right]:
        left -= 1
        right += 1
    print(left, right)

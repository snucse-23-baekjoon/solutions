def factorial(num):
    if not num:
        return 1
    return num * factorial(num - 1)

def combination(num1, num2):
    return factorial(num1)//(factorial(num1 - num2) * factorial(num2))

import sys

repeat = int(sys.stdin.readline().rstrip())
for _ in range(repeat):
    num1, num2 = tuple(map(int, sys.stdin.readline().split()))
    print(combination(max((num1, num2)), min((num1, num2))))
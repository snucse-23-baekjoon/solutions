import sys

repeat = int(sys.stdin.readline().rstrip())
score = list(map(int, sys.stdin.readline().split()))
print(sum(score) * 100 / (repeat * max(score)))
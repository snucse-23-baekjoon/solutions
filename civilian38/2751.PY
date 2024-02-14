import sys

number = int(sys.stdin.readline().rstrip())
arr = [int(sys.stdin.readline().rstrip()) for _ in range(number)]
arr.sort()

any(map(print, arr))
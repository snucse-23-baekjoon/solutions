import sys

n, m = map(int, sys.stdin.readline().split())
dictionary = set()
for _ in range(n):
    dictionary.add(sys.stdin.readline().rstrip())

count = 0
for _ in range(m):
    if sys.stdin.readline().rstrip() in dictionary:
        count += 1
    
print(count)
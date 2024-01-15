def finder(word, target):
    if target in word:
        for index in range(len(word)):
            if word[index:index+len(target)] == target:
                break
        return 1 + finder(word[index+len(target):], target)
    return 0;

import sys
sys.stdin = open('case4.txt')

given = sys.stdin.readline().rstrip()
find = sys.stdin.readline().rstrip()

print(finder(given, find))
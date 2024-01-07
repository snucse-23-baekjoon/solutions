def isgroup(s):
    lst = [0 for i in range(26)]
    for i in range(1, len(s)):
        if s[i - 1] != s[i]:
            lst[ord(s[i - 1]) - ord("a")] = 1
        if lst[ord(s[i]) - ord("a")] == 1:
            return False
    return True

n = int(input())
count = 0
for i in range(n):
    if isgroup(input()):
        count += 1
print(count)

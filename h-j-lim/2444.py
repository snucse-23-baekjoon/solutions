def ispalindrome(s):
    i = 0
    while i <= len(s) // 2:
        if s[i] != s[-1 - i]:
            return 0
        i += 1
    return 1

a = input()
print(ispalindrome(a))
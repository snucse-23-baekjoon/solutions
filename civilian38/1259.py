def is_palindrome(word):
    if len(word) == 0 or len(word) == 1:
        return "yes"
    else:
        if word[0] == word[-1]:
            return is_palindrome(word[1:-1])
        else:
            return "no"

import sys

data = sys.stdin.readline().rstrip()
while data != "0":
    print(is_palindrome(data))
    data = sys.stdin.readline().rstrip()
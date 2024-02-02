import sys


def is_palindrome(x):
    if len(x) <= 1:
        return True
    if x[0] == x[-1]:
        return is_palindrome(x[1: -1])
    else:
        return False


X = sys.stdin.readline().rstrip()
while int(X):
    if is_palindrome(X):
        print('yes')
    else:
        print('no')
    X = sys.stdin.readline().rstrip()

import sys


def is_balanced(test_case):
    i = 0
    n = len(test_case)
    lst = []
    while i < n:
        x = test_case[i]
        if x == '(' or x == '[':
            lst.append(x)
        if x == ')':
            if lst and lst[-1] == '(':
                lst.pop()
            else:
                return False
        if x == ']':
            if lst and lst[-1] == '[':
                lst.pop()
            else:
                return False
        i += 1
    if not lst:
        return True
    else:
        return False


Test_Case = sys.stdin.readline().rstrip()
while Test_Case != '.':
    if is_balanced(Test_Case):
        print('yes')
    else:
        print('no')
    Test_Case = sys.stdin.readline().rstrip()

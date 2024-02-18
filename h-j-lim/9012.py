import sys


def vps(test_case):
    if len(test_case) == 0:
        return True
    if not(test_case[0] == '(' and test_case[-1] == ')'):
        return False
    i = 0
    while test_case[i] == '(':
        i += 1
    test_case.pop(i - 1)
    test_case.pop(i - 1)
    return vps(test_case)


T = int(sys.stdin.readline())
for _ in range(T):
    Test_Case = list(sys.stdin.readline().rstrip())
    if vps(Test_Case):
        print('YES')
    else:
        print('NO')

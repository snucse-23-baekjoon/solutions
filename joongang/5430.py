from sys import stdin
from collections import deque
t = int(stdin.readline())
for _ in range(t):
    p = list(stdin.readline().rstrip())
    n = int(stdin.readline())
    if n:
        lst = deque(map(int, stdin.readline().rstrip()[1:-1].split(',')))
    else:
        stdin.readline()
        lst = deque()
    error = 0
    reverse = 1
    for i in p:
        if i == 'R':
            reverse *= -1
        elif i == 'D':
            if lst:
                if reverse == 1:
                    lst.popleft()
                else:
                    lst.pop()
            else:
                error = 1
                break
    if error:
        print('error')
    else:
        if reverse == -1:
            lst.reverse()
        s = ','.join(map(str, lst))
        print(f'[{s}]')
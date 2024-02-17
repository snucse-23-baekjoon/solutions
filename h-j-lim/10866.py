from collections import deque
import sys


N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    a = command[0]
    if a == 'push_front':
        q.appendleft(int(command[1]))
    if a == 'push_back':
        q.append(int(command[1]))
    if a == 'pop_front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    if a == 'pop_back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])
            q.pop()
    if a == 'size':
        print(len(q))
    if a == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    if a == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    if a == 'back':
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])


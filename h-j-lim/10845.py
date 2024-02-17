from collections import deque
import sys


N = int(sys.stdin.readline())
q = deque()
for _ in range(N):
    command = sys.stdin.readline().rstrip().split()
    a = command[0]
    if a == 'push':
        last = int(command[1])
        q.append(int(command[1]))
    elif a == 'pop':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
            q.popleft()
    elif a == 'size':
        print(len(q))
    elif a == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif a == 'front':
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:  # back
        if len(q) == 0:
            print(-1)
        else:
            print(q[-1])


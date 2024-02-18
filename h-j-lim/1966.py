import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    q1 = list(map(int, sys.stdin.readline().split()))
    q2 = list(range(N))
    find = False
    cnt = 0
    while not find:
        if max(q1) == q1[0]:
            if q2[0] == M:
                cnt += 1
                find = True
            else:
                q1.pop(0)
                q2.pop(0)
                cnt += 1
        else:
            q1.append(q1.pop(0))
            q2.append(q2.pop(0))
    print(cnt)

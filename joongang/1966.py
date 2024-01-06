from sys import stdin
t = int(stdin.readline())
for i in range(t):
    n, m = map(int, stdin.readline().split())
    lst = list(map(int, stdin.readline().split()))
    cnt = 0
    while lst:
        if max(lst) == lst[0]:
            lst = lst[1:]
            cnt += 1
            if m:
                m -= 1
            else:
                break
        else:
            lst = lst[1:] + [lst[0]]
            if m:
                m -= 1
            else:
                m = len(lst) - 1
    print(cnt)
        
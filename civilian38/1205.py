n, t, p = tuple(map(int, input().split()))
ranks = list()
if n:
    ranks = list(reversed(sorted(map(int, input().split()))))

if ranks:
    if len(ranks) >= p:
        if ranks[-1] >= t:
            print(-1)
            ranks = list()
    if ranks:
        if t >= ranks[0]:
            print(1)
        elif len(ranks) == 1:
            print(2)
        else:
            for i in range(len(ranks) - 1):
                if ranks[i] > t >= ranks[i + 1]:
                    print(i + 2)
            if ranks[-1] > t:
                print(len(ranks) + 1)
else:
    print(1)
def check(i, j, n):
    for k in range(9):
        if lst[i][k] == n or lst[k][j] == n:
            return 0
    i = 3*(i//3)
    j = 3*(j//3)
    for w in range(3):
        for h in range(3):
            if lst[i+w][j+h] == n:
                return 0
    return 1

def f(i, j):
    if not lst[i][j]:
        for n in range(1, 10):
            if check(i, j, n):
                lst[i][j] = n
                if j == 8:
                    if i == 8:
                        f(i, j)
                    else:
                        f(i+1, 0)
                else:
                    f(i, j+1)
                lst[i][j] = 0
    elif not (i == 8 and j == 8):
        if j == 8:
            f(i+1, 0)
        else:
            f(i, j+1)
    else:
        for w in range(9):
            for h in range(9):
                print(lst[w][h], end='')
            print()
        exit(0)

from sys import stdin
lst = [list(map(int, list(stdin.readline().rstrip()))) for i in range(9)]
f(0, 0)
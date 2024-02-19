def f(board, direction, cnt):
    if cnt == 5:
        result = 0
        for i in range(n):
            for j in range(n):
                result = max(result, board[i][j])
        return result
    tmp = deepcopy(board)
    if direction == 1:
        for i in range(n):
            fusion = []
            for j in range(1, n):
                move = 1
                while move <= j and not tmp[j-move][i]:
                    tmp[j-move][i] = tmp[j-move+1][i]
                    tmp[j-move+1][i] = 0
                    move += 1
                if move != j+1 and tmp[j-move][i] == tmp[j-move+1][i] and j-move not in fusion:
                    tmp[j-move][i] *= 2
                    tmp[j-move+1][i] = 0
                    fusion.append(j-move)
    elif direction == 2:
        for i in range(n):
            fusion = []
            for j in range(n-2, -1, -1):
                move = 1
                while j+move < n and not tmp[i][j+move]:
                    tmp[i][j+move] = tmp[i][j+move-1]
                    tmp[i][j+move-1] = 0
                    move += 1
                if j+move != n and tmp[i][j+move] == tmp[i][j+move-1] and j+move not in fusion:
                    tmp[i][j+move] *= 2
                    tmp[i][j+move-1] = 0
                    fusion.append(j+move)
    elif direction == 3:
        for i in range(n):
            fusion = []
            for j in range(n-2, -1, -1):
                move = 1
                while j+move < n and not tmp[j+move][i]:
                    tmp[j+move][i] = tmp[j+move-1][i]
                    tmp[j+move-1][i] = 0
                    move += 1
                if j+move != n and tmp[j+move][i] == tmp[j+move-1][i] and j+move not in fusion:
                    tmp[j+move][i] *= 2
                    tmp[j+move-1][i] = 0
                    fusion.append(j+move)
    elif direction == 4:
        for i in range(n):
            fusion = []
            for j in range(1, n):
                move = 1
                while move <= j and not tmp[i][j-move]:
                    tmp[i][j-move] = tmp[i][j-move+1]
                    tmp[i][j-move+1] = 0
                    move += 1
                if move != j+1 and tmp[i][j-move] == tmp[i][j-move+1] and j-move not in fusion:
                    tmp[i][j-move] *= 2
                    tmp[i][j-move+1] = 0
                    fusion.append(j-move)
    return max([f(tmp, 1, cnt+1), f(tmp, 2, cnt+1), f(tmp, 3, cnt+1), f(tmp, 4, cnt+1)])

from sys import stdin
from copy import deepcopy
n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(n)]
print(max([f(board, 1, 0), f(board, 2, 0), f(board, 3, 0), f(board, 4, 0)]))
def dfs(i, bishops, cnt):
    global diag1, diag2, pans
    diag1.add(bishops[i][0] + bishops[i][1])
    diag2.add(bishops[i][0] - bishops[i][1])
    for j in range(i+1, len(bishops)):
        if bishops[j][0]+bishops[j][1] not in diag1 and bishops[j][0]-bishops[j][1] not in diag2:
            dfs(j, bishops, cnt+1)
    pans = max(pans, cnt)
    diag1.remove(bishops[i][0] + bishops[i][1])
    diag2.remove(bishops[i][0] - bishops[i][1])

from sys import stdin
n = int(stdin.readline())
board = [list(map(int, stdin.readline().split())) for i in range(n)]
bishops1 = []
bishops2 = []
for i in range(n):
    for j in range(n):
        if board[i][j]:
            if (i+j)%2:
                bishops1.append((i, j))
            else:
                bishops2.append((i, j))
diag1 = set()
diag2 = set()
ans = 0
pans = 0
for i in range(len(bishops1)):
    dfs(i, bishops1, 1)
ans += pans
pans = 0
for i in range(len(bishops2)):
    dfs(i, bishops2, 1)
ans += pans
print(ans)
import sys
sys.setrecursionlimit(10 ** 6)


def adjacent(r, c):
    global cnt
    if campus_map[r][c] == 'P':
        cnt += 1
    campus_map[r][c] = 'X'
    if r > 0 and campus_map[r - 1][c] != 'X':
        adjacent(r - 1, c)
    if c < M - 1 and campus_map[r][c + 1] != 'X':
        adjacent(r, c + 1)
    if r < N - 1 and campus_map[r + 1][c] != 'X':
        adjacent(r + 1, c)
    if c > 0 and campus_map[r][c - 1] != 'X':
        adjacent(r, c - 1)


N, M = map(int, sys.stdin.readline().split())
campus_map = []
initial_loc = []
found = False
for i in range(N):
    line_to_add = list(sys.stdin.readline().rstrip())
    campus_map.append(line_to_add)
    if not found:
        for j in range(M):
            if line_to_add[j] == 'I':
                initial_loc = [i, j]
                found = True
cnt = 0
adjacent(initial_loc[0], initial_loc[1])
if cnt == 0:
    print('TT')
else:
    print(cnt)

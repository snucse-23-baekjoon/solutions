import sys


def tomatoes(current_level):
    next_level = []
    for tomato in current_level:
        row, col = tomato[0], tomato[1]
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        for direction in directions:
            if 0 <= row + direction[0] < N and 0 <= col + direction[1] < M:
                if visited[row + direction[0]][col + direction[1]] == 0:
                    visited[row + direction[0]][col + direction[1]] = 1
                    next_level.append([row + direction[0], col + direction[1]])
    return next_level


M, N = map(int, sys.stdin.readline().split())
G = []
initial = []
visited = []
for i in range(N):
    to_add = list(map(int, sys.stdin.readline().split()))
    G.append(to_add)
    visited.append(to_add)
    for j in range(M):
        if to_add[j] == 1:
            initial.append([i, j])
current = initial[:]
for i in range(10 ** 6):
    next_to_search = tomatoes(current)
    if not next_to_search:
        ans = i
        break
    else:
        current = next_to_search[:]
done = True
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            done = False
            break
if done:
    print(ans)
else:
    print(-1)

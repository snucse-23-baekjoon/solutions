def bfs(houses, i, j, n):
    global visited
    visited[i][j] = 1
    queue = [(i, j)]
    dx = [1, 0 ,-1, 0]
    dy = [0, 1, 0, -1]
    cnt = 1
    while queue:
        for i in range(4):
            x = queue[0][1] + dx[i]
            y = queue[0][0] + dy[i]
            if x < 0 or x >= n or y < 0 or y >= n:
                continue
            if houses[y][x] and not visited[y][x]:
                queue.append((y, x))
                visited[y][x] = 1
                cnt += 1
        queue.pop(0)
    return cnt

from sys import stdin
n = int(stdin.readline())
houses = [list(map(int, list(stdin.readline().rstrip()))) for i in range(n)]
ans = []
visited = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    for j in range(n):
        if houses[i][j] and not visited[i][j]:
            ans.append(bfs(houses, i, j, n))
ans.sort()
print(len(ans))
for i in ans:
    print(i)
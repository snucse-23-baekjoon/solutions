import sys


N = int(sys.stdin.readline())
game_map = []
result_map = [[0] * N for _ in range(N)]
for _ in range(N):
    game_map.append(list(map(int, sys.stdin.readline().split())))
result_map[0][0] = 1
ans = 0
done = False
while not done:
    done = True
    for i in range(N):
        for j in range(N):
            if result_map[i][j] != 0:
                done = False
                jump = game_map[i][j]
                tmp = result_map[i][j]
                if jump != 0:
                    if i + jump < N:
                        result_map[i + jump][j] += tmp
                    if j + jump < N:
                        result_map[i][j + jump] += tmp
                else:
                    if i == N - 1 and j == N - 1:
                        ans += tmp
                result_map[i][j] = 0
print(ans)

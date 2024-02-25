def hide_and_seek(target, current_level):  # application of bfs
    found = False
    for loc in current_level:
        if loc - 1 == target or loc + 1 == target or 2 * loc == target:
            found = True
            break
        if loc - 1 >= 0 and visited[loc - 1] == 0:
            visited[loc - 1] = 1
            next_level.append(loc - 1)
        if loc + 1 <= 100000 and visited[loc + 1] == 0:
            visited[loc + 1] = 1
            next_level.append(loc + 1)
        if loc <= 50000 and visited[2 * loc] == 0:
            visited[2 * loc] = 1
            next_level.append(2 * loc)
    if found:
        return True
    else:
        return False


N, K = map(int, input().split())
if N == K:
    print(0)
else:
    visited = [0] * 100001
    visited[N] = 1
    level = [N]
    ans = 0
    for i in range(1, 100001):
        next_level = []
        if hide_and_seek(K, level):
            ans = i
            break
        level = next_level[:]
    print(ans)

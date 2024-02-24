import sys


def kevin_bacon(current_level, visited, level, bacon_num):
    next_level = []
    for person in current_level:
        for acq in adjacency_list[person]:
            if acq not in visited:
                visited.append(acq)
                next_level.append(acq)
                bacon_num += level
    if next_level:
        return kevin_bacon(next_level, visited, level + 1, bacon_num)
    else:
        return bacon_num


N, M = map(int, sys.stdin.readline().split())
adjacency_list = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if b not in adjacency_list[a]:
        adjacency_list[a].append(b)
        adjacency_list[b].append(a)
kevin_bacon_list = [0]
for i in range(1, N + 1):
    kevin_bacon_list.append(kevin_bacon([i], [i], 1, 0))
min_index = 1
min_num = kevin_bacon_list[1]
for i in range(1, N + 1):
    if kevin_bacon_list[i] < min_num:
        min_num = kevin_bacon_list[i]
        min_index = i
print(min_index)

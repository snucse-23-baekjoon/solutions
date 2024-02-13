N, M = map(int, input().split())
trees = list(map(int, input().split()))
dict_trees = {}
for tree in trees:
    if tree not in dict_trees.keys():
        dict_trees[tree] = 1
    else:
        dict_trees[tree] += 1
lower_bound, upper_bound = 0, max(trees)
while lower_bound + 1 < upper_bound:
    tmp = 0
    mid = (lower_bound + upper_bound) // 2
    for height in dict_trees.keys():
        if height > mid:
            tmp += dict_trees[height] * (height - mid)
    if tmp >= M:
        lower_bound = mid
    else:
        upper_bound = mid
print(lower_bound)

import sys
sys.stdin = open("../input.txt", 'r')

N = int(sys.stdin.readline())
candy_box = [0 for _ in range(1_000_000)]
seg_tree = [0 for _ in range(2_097_151)]  # 2 * 2^20 - 1

def find_index(index_in_arr, left=0, right=1_000_000, index=0):
    if right - left == 1:
        return index
    center = (left + right - 1) // 2 + 1
    if index_in_arr < center:
        return find_index(index_in_arr, left, center, 2 * index + 1)
    else:
        return find_index(index_in_arr, center, right, 2 * index + 2)

def update_seg_tree(tree, index_in_arr, diff):
    index = find_index(index_in_arr)
    while index > 0:
        tree[index] += diff
        index = (index - 1) // 2
    tree[0] += diff

def search_seg_tree(tree, total, left=0, right=1_000_000, index=0):
    if right - left == 1:
        return left
    center = (left + right - 1) // 2 + 1
    if total <= tree[2 * index + 1]:
        return search_seg_tree(tree, total, left, center, 2 * index + 1)
    else:
        total -= tree[2 * index + 1]
        return search_seg_tree(tree, total, center, right, 2 * index + 2)

for _ in range(N):
    query = list(map(int, sys.stdin.readline().split()))
    if query[0] == 1:
        index = search_seg_tree(seg_tree, query[1])
        update_seg_tree(seg_tree, index, -1)
        print(index + 1)
    if query[0] == 2:
        update_seg_tree(seg_tree, query[1] - 1, query[2])

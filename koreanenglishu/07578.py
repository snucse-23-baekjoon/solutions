import sys
sys.stdin = open("../input.txt", 'r')

N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]
arr1 = list(zip(map(int, sys.stdin.readline().split()), range(N)))
arr2 = list(zip(map(int, sys.stdin.readline().split()), range(N)))

arr1.sort(key=lambda x: x[0])
arr2.sort(key=lambda x: x[0])
for i in range(N):
    arr[arr1[i][1]] = arr2[i][1]

M = 1
while M < N:
    M *= 2
tree = [0 for _ in range(2 * M - 1)]

def find_index(index_in_arr, left=0, right=N, index=0):
    if right - left == 1:
        return index
    center = (left + right - 1) // 2 + 1
    if index_in_arr < center:
        return find_index(index_in_arr, left, center, 2 * index + 1)
    else:
        return find_index(index_in_arr, center, right, 2 * index + 2)

def update_seg_tree(tree, index_in_arr):
    index = find_index(index_in_arr)
    while index > 0:
        tree[index] += 1
        index = (index - 1) // 2
    tree[0] += 1

def find_sum(tree, start, end, left=0, right=N, index=0):
    if start == end:
        return 0
    if start == left and end == right:
        return tree[index]
    center = (left + right - 1) // 2 + 1
    if end <= center:
        return find_sum(tree, start, end, left, center, 2 * index + 1)
    elif start >= center:
        return find_sum(tree, start, end, center, right, 2 * index + 2)
    else:
        return find_sum(tree, start, center, left, center, 2 * index + 1) \
            + find_sum(tree, center, end, center, right, 2 * index + 2)

count = 0
for n in arr:
    count += find_sum(tree, n + 1, N)
    update_seg_tree(tree, n)
print(count)

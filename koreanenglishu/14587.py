import sys
sys.stdin = open("../input.txt", 'r')

arr = []
N = int(sys.stdin.readline())
for _ in range(N):
    x, h = map(int, sys.stdin.readline().split())
    arr.append((x, h))

arr.sort()
tree = [((0, 0), (0, 0))] * (4 * N)

def binary_search(x):
    left, right = 0, N
    if x < arr[0][0]:
        return -1
    while right - left > 1:
        center = (left + right - 1) // 2 + 1
        if x < arr[center][0]:
            right = center
        else:
            left = center
    return left

def build_tree(left=0, right=N, index=0):
    if right - left == 1:
        tree[index] = (
            (binary_search(arr[left][0] - arr[left][1] - 1) + 1, left),
            (binary_search(arr[left][0] + arr[left][1]), left)
        )
    else:
        center = (left + right - 1) // 2 + 1
        build_tree(left, center, 2 * index + 1)
        build_tree(center, right, 2 * index + 2)
        tree[index] = (
            min(tree[2 * index + 1][0], tree[2 * index + 2][0]),
            max(tree[2 * index + 1][1], tree[2 * index + 2][1])
        )

def update_tree(pos, value):
    left, right, index = 0, N, 0
    while right - left > 1:
        center = (left + right - 1) // 2 + 1
        if pos < center:
            right, index = center, 2 * index + 1
        else:
            left, index = center, 2 * index + 2

    while index > 0:
        tree[index] = (
            min(tree[index][0], value[0]),
            max(tree[index][1], value[1])
        )
        index = (index - 1) // 2

def search_tree(start, end, left=0, right=N, index=0):
    if start == left and end == right:
        return tree[index]
    center = (left + right - 1) // 2 + 1
    if end <= center:
        return search_tree(start, end, left, center, 2 * index + 1)
    elif start >= center:
        return search_tree(start, end, center, right, 2 * index + 2)
    else:
        a1, b1 = search_tree(start, center, left, center, 2 * index + 1)
        a2, b2 = search_tree(center, end, center, right, 2 * index + 2)
        return min(a1, a2), max(b1, b2)

build_tree()
leftmost = [i for i in range(N)]
rightmost = [i for i in range(N)]

for i in range(N):
    left = binary_search(arr[i][0] - arr[i][1] - 1) + 1
    leftmost[i] = leftmost[search_tree(left, i + 1)[0][1]]

for i in range(N - 1, -1, -1):
    right = binary_search(arr[i][0] + arr[i][1])
    rightmost[i] = rightmost[search_tree(i, right + 1)[1][1]]

dp_left = leftmost
dp_right = [i for i in range(N)]
for i in range(N - 1, -1, -1):
    dp_right[rightmost[i]] = i

temp = N
for i in range(N - 1, -1, -1):
    if temp > dp_right[i]:
        temp = dp_right[i]
    else:
        dp_right[i] = temp

dp = [0] * N
for i in range(N):
    temp1 = dp[dp_left[i] - 1] if dp_left[i] > 0 else 0
    temp2 = dp[dp_right[i] - 1] if dp_right[i] > 0 else 0
    dp[i] = 1 + min(temp1, temp2)

print(dp[-1])
# print(leftmost)
# print(rightmost)

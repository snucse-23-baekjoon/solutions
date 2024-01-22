from sys import stdin
from copy import deepcopy
stdin = open("../input.txt", 'r')

names = []
for _ in range(int(stdin.readline())):
    names.append(stdin.readline().rstrip())

# GENERATE SUFFIX ARRAY
suffix_array = []
for i in range(len(names)):
    for j in range(len(names[i])):
        suffix_array.append((i, j))
n = len(suffix_array)

group, next_group = [], []
for s in names:
    group.append([ord(c) for c in s])
    next_group.append([0] * len(s))

def compare_key(x): return (
    group[x[0]][x[1]], group[x[0]][x[1] + t]
    if x[1] + t < len(names[x[0]]) else -1
)

t = 1
while t < n:
    suffix_array.sort(key=compare_key)
    for i in range(n - 1):
        x, y = suffix_array[i:i + 2]
        next_group[y[0]][y[1]] = next_group[x[0]][x[1]]
        if compare_key(x) < compare_key(y):
            next_group[y[0]][y[1]] += 1

    x = suffix_array[-1]
    if next_group[x[0]][x[1]] == n - 1: break
    group = deepcopy(next_group); t *= 2

# GENERATE LCP ARRAY
lcp_array = [0] * n
inv_suffix_array = deepcopy(group)
for i, x in enumerate(suffix_array):
    inv_suffix_array[x[0]][x[1]] = i

for i in range(len(names)):
    c = 0
    for j in range(len(names[i])):
        k = inv_suffix_array[i][j]
        if k == 0: c = 0; continue
        l, m = suffix_array[k - 1]
        while j + c < len(names[i]) and m + c < len(names[l]) \
            and names[i][j + c] == names[l][m + c]: c += 1
        lcp_array[k] = c
        if c > 0: c -= 1

# SEGMENT TREE AND ITS OPERATION
class SegTree:
    def __init__(self, size, oper):
        nodes = 1
        while nodes < size: nodes <<= 1
        nodes = (nodes << 1) - 1
        self.tree = [-2] * nodes
        self.oper = oper

    def update(self, i, val):
        l, r, j = 0, n, 0
        while r - l > 1:
            self.tree[j] = self.oper(self.tree[j], val)
            c = (l + r + 1) // 2
            if i < c: r, j = c, 2 * j + 1
            else: l, j = c, 2 * j + 2
        self.tree[j] = self.oper(self.tree[j], val)

    def find(self, s, e, l=0, r=n, j=0):
        if s == e: return 0
        if s == l and e == r: return self.tree[j]
        c = (l + r + 1) // 2
        if e <= c: return self.find(s, e, l, c, 2 * j + 1)
        if s >= c: return self.find(s, e, c, r, 2 * j + 2)
        return self.oper(
            self.find(s, c, l, c, 2 * j + 1),
            self.find(c, e, c, r, 2 * j + 2)
        )

def oper(x, y):
    if x == -2: return y
    if y == -2: return x
    if x == y: return x
    return -1

tree = SegTree(n, oper)
for i in range(n):
    tree.update(i, suffix_array[i][0])

stack = []
answer = [0] * len(names)
for i in range(n + 1):
    if i < n:
        j, k = suffix_array[i - 1]
        l, m = suffix_array[i]
        overlap = min(lcp_array[i],
            len(names[j]) - k, len(names[l]) - m)
        answer[l] += len(names[l]) - m - overlap
    else: overlap = 0

    while len(stack) > 1 and overlap < stack[-1][1]:
        diff = stack[-1][1] - max(stack[-2][1], overlap)
        if tree.find(stack[-1][0], i) < 0:
            answer[suffix_array[stack[-1][0]][0]] -= diff
        if stack[-2][1] >= overlap: stack.pop()
        else: stack[-1][1] -= diff
    stack.append([i - 1, overlap])

print(*answer, sep='\n')

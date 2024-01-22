from sys import stdin
stdin = open("../input.txt", 'r')

i = 0
string, check_index = [], []
for c in stdin.readline().rstrip():
    if c == '?': check_index.append(i)
    else: string.append(c); i += 1
string = ''.join(reversed(string))
n = len(string)

# GENERATE SUFFIX ARRAY
suffix_array = [i for i in range(n)]
group = [ord(c) for c in string]
next_group = [0] * (n + 1)

t = 1
while t < n:
    suffix_array.sort(key=lambda x: (
        group[x], group[x + t] if x + t < n else -1
    ))

    for i in range(n - 1):
        j, k = suffix_array[i:i + 2]
        next_group[k] = next_group[j]
        if (group[j], group[j + t] if j + t < n else -1) < \
                (group[k], group[k + t] if k + t < n else -1):
            next_group[k] += 1

    if next_group[n - 1] == n - 1: break
    group = next_group[:]; t *= 2

# GENERATE LCP ARRAY
lcp_array = [0] * n
inv_suffix_array = [0] * n
for i in range(n):
    inv_suffix_array[suffix_array[i]] = i

i = 0
for j in range(n):
    if inv_suffix_array[j] == 0:
        i = 0; continue
    k = suffix_array[inv_suffix_array[j] - 1]; m = max(j, k)
    while i + m < n and string[i + j] == string[i + k]: i += 1
    lcp_array[inv_suffix_array[j]] = i
    if i > 0: i -= 1

# CLASS OF SEGMENT TREE
class SegTree:
    def __init__(self, size, oper):
        self.tree = [0] * size
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

substrings = SegTree(1 << 19, lambda x, y: x + y)
for i in range(n): substrings.update(
    suffix_array[i], n - suffix_array[i] - lcp_array[i]
)

max_suffix_index = SegTree(1 << 19, lambda x, y: max(x, y))
for i in range(n): max_suffix_index.update(i, suffix_array[i])

stack = []
lcp_array.append(0)
for i in range(n + 1):
    while len(stack) > 1 and lcp_array[i] < stack[-1][1]:
        j = max_suffix_index.find(stack[-1][0], i)
        diff = stack[-1][1] - max(stack[-2][1], lcp_array[i])
        substrings.update(suffix_array[stack[-1][0]], -diff)
        substrings.update(j, diff)
        if stack[-2][1] >= lcp_array[i]: stack.pop()
        else: stack[-1][1] -= diff
    stack.append([i - 1, lcp_array[i]])

for i in check_index:
    print(substrings.find(n - i, n))

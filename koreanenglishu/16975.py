from sys import stdin
stdin = open("../input.txt", 'r')

class LazySegTree:
    def __init__(self, size):
        nodes = 1
        while nodes < size: nodes <<= 1
        nodes = (nodes << 1) - 1
        self.tree = [0] * nodes
        self.lazy = [0] * nodes
        self.size = size

    def update_lazy(self, l, r, j):
        if self.lazy[j]:
            self.tree[j] += (r - l) * self.lazy[j]
            if r - l > 1:
                self.lazy[2 * j + 1] += self.lazy[j]
                self.lazy[2 * j + 2] += self.lazy[j]
        self.lazy[j] = 0

    def update(self, i, val):
        l, r, j = 0, self.size, 0
        while r - l > 1:
            self.update_lazy(l, r, j)
            self.tree[j] += val
            c = (l + r + 1) // 2
            if i < c: r, j = c, 2 * j + 1
            else: l, j = c, 2 * j + 2
        self.update_lazy(l, r, j)
        self.tree[j] += val

    def update_range(self, s, e, val, l=0, r=0, j=0):
        if not r: r = self.size
        self.update_lazy(l, r, j)
        self.tree[j] += (e - s) * val
        if r - l == 1: return
        if s == l and e == r:
            self.lazy[2 * j + 1] += val
            self.lazy[2 * j + 2] += val
            return
        c = (l + r + 1) // 2
        if e <= c: return self.update_range(s, e, val, l, c, 2 * j + 1)
        if s >= c: return self.update_range(s, e, val, c, r, 2 * j + 2)
        self.update_range(s, c, val, l, c, 2 * j + 1)
        self.update_range(c, e, val, c, r, 2 * j + 2)

    def find(self, s, e, l=0, r=0, j=0):
        if not r: r = self.size
        self.update_lazy(l, r, j)
        if s == e: return 0
        if s == l and e == r: return self.tree[j]
        c = (l + r + 1) // 2
        if e <= c: return self.find(s, e, l, c, 2 * j + 1)
        if s >= c: return self.find(s, e, c, r, 2 * j + 2)
        return self.find(s, c, l, c, 2 * j + 1) \
            + self.find(c, e, c, r, 2 * j + 2)

n = int(stdin.readline())
tree = LazySegTree(n)
arr = map(int, stdin.readline().split())
for i in range(n): tree.update(i, next(arr))

for _ in range(int(stdin.readline())):
    a, *q = map(int, stdin.readline().split())
    if a == 1:
        i, j, k = q[0] - 1, q[1] - 1, q[2]
        tree.update_range(i, j + 1, k)
    else:  # a == 2
        x = q[0] - 1
        print(tree.find(x, x + 1))

from sys import stdin
import random


class SkipNode:
    def __init__(self, height, val, idx):
        self.nexts = [None] * height
        self.prevs = [None] * height
        self.val = val
        self.idx = idx

    def delete(self):
        for i in range(len(self.nexts)):
            l = self.prevs[i]
            r = self.nexts[i]
            l.nexts[i] = r
            r.prevs[i] = l

    def nxt(self): return self.nexts[0]


class SkipList:
    def __init__(self, height):
        self.height = height
        self.head = SkipNode(height, None, 0)
        self.tail = SkipNode(height, None, 0)
        self.head.nexts = [self.tail] * height
        self.tail.prevs = [self.head] * height

    def __iter__(self):
        ptr = self.head.nxt()
        while ptr.nxt():
            yield ptr
            ptr = ptr.nxt()

    def gen_height(self):
        h = 1
        while h < self.height and random.random() < 0.5: h += 1
        return h

    # last node, in each height, such that the predicate is true
    def search(self, pred):
        res = []
        ptr = self.head
        for i in range(self.height - 1, -1, -1):
            while 1:
                nxt = ptr.nexts[i]
                if nxt == self.tail or not pred(nxt): break
                ptr = nxt
            res.append(ptr)
        return res[::-1]

    # insert a node after the last node whose predicate is true
    def insert(self, pred, node):
        nodes = self.search(pred)
        for i in range(len(node.nexts)):
            l = nodes[i]
            r = l.nexts[i]
            l.nexts[i] = node
            node.nexts[i] = r
            r.prevs[i] = node
            node.prevs[i] = l

    # remove the last node whose predicate is true
    def remove(self, pred):
        node = self.search(pred)[0]
        assert node != self.head
        node.delete()

    def insert_first(self, val):
        self.insert((lambda node: False), val)

    def insert_last(self, val):
        self.insert((lambda node: True), val)

    def insert_increasing(self, val):
        self.insert((lambda node: node.val <= val), val)

    def insert_decreasing(self, val):
        self.insert((lambda node: node.val >= val), val)


########################

class Pnt:
    def __init__(self, x, y): self.x = x; self.y = y

    # Basic ops
    def sq(self): return self.x ** 2 + self.y ** 2
    def __abs__(self): return (self.x ** 2 + self.y ** 2) ** .5
    def __le__(self, o): return (self.x, self.y) <= (o.x, o.y)

    # Scalar ops
    def __mul__(self, d): return Pnt(d * self.x, d * self.y)
    def __rmul__(self, d): return Pnt(self.x * d, self.y * d)
    def __truediv__(self, d): return Pnt(self.x / d, self.y / d)
    def __floordiv__(self, d): return Pnt(self.x // d, self.y // d)

    # Vector ops
    def __eq__(self, q): return self.x == q.x and self.y == q.y
    def __add__(self, q): return Pnt(self.x + q.x, self.y + q.y)
    def __sub__(self, q): return Pnt(self.x - q.x, self.y - q.y)


class Seg:
    def __init__(self, a, b):
        if a.y < b.y: a, b = b, a
        if a.y == b.y and a.x > b.x: a, b = b, a
        self.u = a
        self.d = b

    def __repr__(self):
        return f"{self.u}--{self.d}"

    def point_is_right(self, p):
        return ccw(self.u, self.d, p) == 1

    def intersects(self, seg):
        return bool(seg_inters(self.u, self.d, seg.u, seg.d))


def sgn(x): return (0<x) - (x<0)
def dot(p, q): return p.x*q.x + p.y*q.y
def cross(p, q): return p.x*q.y - p.y*q.x
def orient(a, b, c): return cross(b-a, c-a) # >0 ccw
def ccw(a, b, c): return sgn(cross(b-a, c-a)) # 1 ccw

def on_seg(a, b, p):
    return orient(a,b,p) == 0 and dot(a-p, b-p) <= 0

def seg_inter_proper(a, b, c, d):
    oa, ob = orient(c,d,a), orient(c,d,b)
    oc, od = orient(a,b,c), orient(a,b,d)
    if oa*ob >= 0 or oc*od >= 0: return False
    return (a*ob - b*oa) / (ob-oa)

def seg_inters(a, b, c, d):
    res = []
    P = seg_inter_proper(a, b, c, d)
    if P: res.append(P)
    if on_seg(c,d,a): res.append(a)
    if on_seg(c,d,b): res.append(b)
    if c!=a and c!=b and on_seg(a,b,c): res.append(c)
    if d!=a and d!=b and on_seg(a,b,d): res.append(d)
    return res

def die(): print(1); exit()
stdin = open("../input.txt", 'r')

n = int(stdin.readline())
ev = []  # -1 add, 0 horizontal, 1 remove
nds = []
S = SkipList(17)
for i in range(1, n + 1):
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    p1, p2 = Pnt(x1, y1), Pnt(x2, y2)
    node = SkipNode(S.gen_height(), Seg(p1, p2), i); nds.append(node)
    ev.extend([(max(y1, y2), -1, node), (min(y1, y2), 1, node)])
ev.sort(key=lambda T: (-T[0], T[1]))

for y, ety, node in ev:
    if ety == -1:  # ADD
        S.insert((lambda N: N.val.point_is_right(node.val.u)), node)
        l, r = node.prevs[0], node.nexts[0]
        if l.val and l.val.intersects(node.val):
            node1, node2 = l, node; break
        if r.val and r.val.intersects(node.val):
            node1, node2 = node, r; break
    elif ety == 1:  # REM
        l, r = node.prevs[0], node.nexts[0]
        if l.val and r.val and l.val.intersects(r.val):
            node1, node2 = l, r; break
        node.delete()

flag1, flag2 = False, False
for node in nds:
    if node.idx in {0, node1.idx, node2.idx}: continue
    if not flag1 and node1.val.intersects(node.val): flag1 = True
    if not flag2 and node2.val.intersects(node.val): flag2 = True
    if all([flag1, flag2]): break

if not flag1 and not flag2: print(min(node1.idx, node2.idx))
elif flag1: print(node1.idx)
elif flag2: print(node2.idx)

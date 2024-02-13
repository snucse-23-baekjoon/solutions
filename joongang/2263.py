def preorder(in1, in2, post1, post2):
    root = postorder[post2-1]
    print(root, end=' ')
    idx = inorder_d[root]
    b = idx - in1
    if in1 < idx:
        preorder(in1, idx, post1, post1+b)
    if idx+1 < in2:
        preorder(idx+1, in2, post1+b, post2-1)

import sys
from sys import stdin
sys.setrecursionlimit(10**9)
n = int(stdin.readline())
inorder = list(map(int, stdin.readline().split()))
postorder = list(map(int, stdin.readline().split()))
inorder_d = {inorder[i]: i for i in range(n)}
preorder(0, n, 0, n)
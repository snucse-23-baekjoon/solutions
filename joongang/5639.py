def postord(v):
    if v in tree:
        if tree[v][0] != 0:
            postord(tree[v][0])
        if tree[v][1] != 0:
            postord(tree[v][1])
    print(v)

import sys
from sys import stdin
sys.setrecursionlimit(10**5)
tree = dict()
node = int(stdin.readline())
root = node
stack = [node]
while 1:
    try:
        sub = int(stdin.readline())
    except:
        break
    if node > sub:
        tree[node] = [sub]
        stack.append(sub)
    else:
        while 1:
            if stack and stack[-1] < sub:
                tmp = stack.pop()
            else:
                if tmp in tree:
                    tree[tmp].append(sub)
                else:
                    tree[tmp] = [0, sub]
                stack.append(sub)
                break
    node = sub
for i in tree:
    if len(tree[i]) == 1:
        tree[i] = [tree[i][0], 0]
postord(root)
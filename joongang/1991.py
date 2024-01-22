def preord(tree, root):
    if '.' not in tree[root]:
        return [root] + preord(tree, tree[root][0]) + preord(tree, tree[root][1])
    if tree[root][0] != '.' and tree[root][1] == '.':
        return [root] + preord(tree, tree[root][0])
    if tree[root][1] != '.' and tree[root][0] == '.':
        return [root] + preord(tree, tree[root][1])
    return [root]

def inord(tree, root):
    if '.' not in tree[root]:
        return inord(tree, tree[root][0]) + [root] + inord(tree, tree[root][1])
    if tree[root][0] != '.' and tree[root][1] == '.':
        return inord(tree, tree[root][0]) + [root]
    if tree[root][1] != '.' and tree[root][0] == '.':
        return [root] + inord(tree, tree[root][1])
    return [root]

def postord(tree, root):
    if '.' not in tree[root]:
        return postord(tree, tree[root][0]) + postord(tree, tree[root][1]) + [root]
    if tree[root][0] != '.' and tree[root][1] == '.':
        return postord(tree, tree[root][0]) + [root]
    if tree[root][1] != '.' and tree[root][0] == '.':
        return postord(tree, tree[root][1]) + [root]
    return [root]

from sys import stdin
n = int(stdin.readline())
tree = dict()
for i in range(n):
    root, l, r = stdin.readline().rstrip().split()
    tree[root] = (l, r)
root = 'A'
print(''.join(preord(tree, root)))
print(''.join(inord(tree, root)))
print(''.join(postord(tree, root)))
from sys import stdin
stdin = open("../input.txt", 'r')

MAX_BITS = 30
trie = [[], []]

def query1(x):
    curr = trie
    for i in range(MAX_BITS - 1, -1, -1):
        b = int(bool(x & (1 << i)))
        if not curr[b]:
            curr[b] = [[], []] if i else [0]
        curr = curr[b]
    curr[0] += 1

def query2(x):
    bb = 0
    curr = branch = trie
    for i in range(MAX_BITS - 1, -1, -1):
        b = int(bool(x & (1 << i)))
        if curr[0] and curr[1]:
            branch, bb = curr, b
        curr = curr[b]
    curr[0] -= 1
    if not curr[0]:
        branch[bb] = []

def query3(x):
    res = 0
    curr = trie
    for i in range(MAX_BITS - 1, -1, -1):
        b = int(bool(x & (1 << i)))
        if curr[1 - b]:
            res += 1 << i
            curr = curr[1 - b]
        else:
            curr = curr[b]
    print(res)

query1(0)
for _ in range(int(stdin.readline())):
    a, x = map(int, stdin.readline().split())
    if a == 1:
        query1(x)
    if a == 2:
        query2(x)
    if a == 3:
        query3(x)

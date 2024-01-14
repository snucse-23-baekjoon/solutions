from sys import stdin
stdin = open("../input.txt", 'r')

class Node:
    def __init__(self, key):
        self.key = key
        self.flag = 0
        # 0: not end / wildcard available
        # 1: end / wildcard available
        # 2: not end / wildcard unavailable
        # 3: end / wildcard unavailable
        # 4: not removable
        self.end = False
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node(None)

    def insert(self, string):
        curr = self.root
        for c in string:
            if c not in curr.child:
                curr.child[c] = Node(c)
            curr = curr.child[c]
        curr.flag = 1

    def mark(self, string):
        curr = self.root
        for c in string:
            if curr.flag < 2:
                curr.flag += 2
            if c not in curr.child:
                return None
            curr = curr.child[c]
        curr.flag = 4

    def dfs(self):
        count = 0
        queue = [self.root]
        while queue:
            curr = queue.pop()
            if curr.flag < 2 or curr.flag == 3:
                count += 1
            if curr.flag > 1:
                for key in curr.child:
                    queue.append(curr.child[key])
        return count

for _ in range(int(stdin.readline())):
    trie = Trie()
    for __ in range(int(stdin.readline())):
        trie.insert(stdin.readline().rstrip())
    for __ in range(int(stdin.readline())):
        trie.mark(stdin.readline().rstrip())
    print(trie.dfs())

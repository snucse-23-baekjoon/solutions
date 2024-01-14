from sys import stdin
stdin = open("../input.txt", 'r')

class Node:
    def __init__(self):
        self.words = 0
        self.end = False
        self.child = dict()

class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, string):
        curr = self.root
        for c in string:
            curr.words += 1
            if c not in curr.child:
                curr.child[c] = Node()
            curr = curr.child[c]
        curr.end = True

    def dfs(self):
        queue = list(self.root.child.values())
        count = self.root.words
        while queue:
            curr = queue.pop()
            if curr.end or len(curr.child) > 1:
                count += curr.words
            queue.extend(curr.child.values())
        return count

while True:
    N = stdin.readline()
    if not N:
        break
    N = int(N)
    trie = Trie()
    for _ in range(N):
        trie.insert(stdin.readline().rstrip())
    print(f"{trie.dfs() / N:.2f}")

from sys import stdin
stdin = open("../input.txt", 'r')

class Node:
    def __init__(self, key):
        self.key = key
        self.child = {}

class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, arr_word):
        curr = self.head
        for word in arr_word:
            if word not in curr.child:
                curr.child[word] = Node(word)
            curr = curr.child[word]

trie = Trie()
N = int(stdin.readline())
for _ in range(N):
    arr = stdin.readline().split()
    trie.insert(arr[1:])

queue = [(trie.head, -1)]
while queue:
    curr, depth = queue.pop()
    if depth >= 0:
        print("--" * depth + curr.key)
    next_keys = list(curr.child.keys())
    next_keys.sort()
    while next_keys:
        next_word = next_keys.pop()
        queue.append((curr.child[next_word], depth + 1))

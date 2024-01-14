from sys import stdin
stdin = open("../input.txt", 'r')

MAX_BITS = 30
trie = [[], []]

def insert(x):
    curr = trie
    for i in range(MAX_BITS - 1, -1, -1):
        b = int(bool(x & (1 << i)))
        if not curr[b]:
            curr[b] = [[], []] if i else True
        curr = curr[b]

def search(x):
    res = 0
    curr = trie
    for i in range(MAX_BITS - 1, -1, -1):
        b = int(bool(x & (1 << i)))
        if curr[1 - b]:
            res += 1 << i
            curr = curr[1 - b]
        else:
            curr = curr[b]
    return res

_ = int(stdin.readline())
nums = map(int, stdin.readline().split())
insert(next(nums))

ans = 0
for x in nums:
    ans = max(ans, search(x))
    insert(x)

print(ans)

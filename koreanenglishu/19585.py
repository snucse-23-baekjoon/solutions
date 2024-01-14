from sys import stdin
stdin = open("../input.txt", 'r')

C, N = map(int, stdin.readline().split())
color_trie = dict(end=dict())
name_set = set()

for _ in range(C):
    curr = color_trie
    for c in stdin.readline().rstrip():
        curr[c] = curr.get(c, dict(end=dict()))
        curr = curr[c]
    curr["end"][None] = None  # bool(curr["end"]) == True

for _ in range(N):
    name_set.add(stdin.readline().rstrip())

Q = int(stdin.readline())
for _ in range(Q):
    string = stdin.readline().rstrip()
    curr = color_trie
    result = "No"
    for i, c in enumerate(string):
        if c not in curr:
            break
        curr = curr[c]
        if curr["end"] and string[i + 1:] in name_set:
            result = "Yes"
            break
    print(result)

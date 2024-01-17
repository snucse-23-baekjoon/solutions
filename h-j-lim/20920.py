import sys


N, M = map(int, sys.stdin.readline().split())
word_count = {}
for _ in range(N):
    word = sys.stdin.readline().rstrip()
    if len(word) >= M:
        if word not in word_count:
            word_count[word] = 1
        else:
            word_count[word] += 1
L1 = list(word_count.keys())
L1.sort(key=lambda x: word_count[x], reverse=True)
L2 = []
i = 0
while i < len(L1):
    j = i
    while j < len(L1) - 1 and word_count[L1[j]] == word_count[L1[j + 1]]:
        j += 1
    tmp = L1[i:j + 1]
    tmp.sort(key=lambda x: len(x), reverse=True)
    L2.append(tmp)
    i = j + 1
L3 = []
for small_list in L2:
    i = 0
    while i < len(small_list):
        j = i
        while j < len(small_list) - 1 and len(small_list[j]) == len(small_list[j + 1]):
            j += 1
        tmp = small_list[i: j + 1]
        tmp.sort()
        L3.extend(tmp)
        i = j + 1
for word in L3:
    print(word)

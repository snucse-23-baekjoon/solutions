from sys import stdin
from copy import deepcopy
stdin = open("../input.txt", 'r')

def push(mat, x, y):
    for dx, dy in [
        (0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)
    ]:
        if 0 <= x + dx < 10 and 0 <= y + dy < 10:
            mat[x + dx][y + dy] ^= 1

arr = []
for _ in range(10):
    arr.append(list(map(
        lambda x: 1 if x == 'O' else 0,
        stdin.readline().rstrip()
    )))

ans = 101
for b in range(1024):
    cnt = 0
    mat = deepcopy(arr)
    for j in range(10):
        if b & (1 << j):
            push(mat, 0, j)
            cnt += 1
    for i in range(1, 10):
        for j in range(10):
            if mat[i - 1][j]:
                push(mat, i, j)
                cnt += 1
    if not any(map(any, mat)):
        ans = min(ans, cnt)

print(ans if ans < 101 else -1)

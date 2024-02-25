from sys import stdin
from itertools import combinations
stdin = open("../input.txt", "r")

N = int(stdin.readline().rstrip()); K = 3
arrs = [[0] * (N + 1) for _ in range(K)]
arrs[0][1:] = list(map(int, stdin.readline().split()))
ans = [(1, 1) for _ in range(K)]
tar = list(range(N + 1))

def find(arr):
    s = e = 0
    for i in range(N + 1):
        if i != arr[i]:
            s = i; break
    if not s: return 1, 1
    for i in range(N, -1, -1):
        if i != arr[i]:
            e = i; break
    return s, e

def interval(arr, start, end):
    ret = []; s = start
    while s <= end:
        ret.append(s); e = s
        while e < end and abs(
            arr[e + 1] - arr[e]) == 1: e += 1
        ret.append(e); s = e + 1
    return ret

def reverse(arr, start, end):
    return arr[:start] + list(reversed(
        arr[start:end + 1])) + arr[end + 1:]

def solve(depth):
    start, end = find(arrs[depth])
    if depth == K - 1:
        ans[depth] = start, end
        if tar == reverse(arrs[depth], *ans[depth]):
            for i in range(K): print(*ans[i])
            exit(0)
        return

    for s, e in combinations(interval(
            arrs[depth], start, end), 2):
        ans[depth] = min(s, e), max(s, e)
        arrs[depth + 1] = reverse(arrs[depth], *ans[depth])
        solve(depth + 1)

solve(0)

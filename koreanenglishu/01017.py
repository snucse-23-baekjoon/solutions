import sys
sys.stdin = open("../input.txt", 'r')

def dfs(i):
    if visited[i]:
        return False
    visited[i] = True

    for j in graph[i]:
        if match[j] == -1 or dfs(match[j]):
            match[j] = i
            return True
    return False

is_prime = [True] * 2000
for p in range(2, 45):
    if is_prime[p]:
        m = 2
        while m * p < 2000:
            is_prime[m * p] = False
            m += 1

N = int(sys.stdin.readline())
arr = map(int, sys.stdin.readline().split())

arr1, arr2 = [], []
arr1.append(next(arr))
rem = arr1[0] % 2
for n in arr:
    if n % 2 == rem:
        arr1.append(n)
    else:
        arr2.append(n)

if len(arr1) != len(arr2):
    print(-1)
    exit(0)

M = N // 2
graph = [[] for _ in range(M)]
for i in range(M):
    for j in range(M):
        if is_prime[arr1[i] + arr2[j]]:
            graph[i].append(j)

answer = []
for i in graph[0]:
    match = [-1] * M
    match[i] = 0
    flag = True
    for j in range(1, M):
        visited = [False] * M
        visited[0] = True
        if not dfs(j):
            flag = False
            break
    if flag:
        answer.append(arr2[i])

answer.sort()
if answer:
    print(*answer, sep=' ')
else:
    print(-1)

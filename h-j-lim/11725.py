import sys


N = int(sys.stdin.readline())
E = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    a, b = map(int, sys.stdin.readline().split())
    E[a].append(b)
    E[b].append(a)
A = [0] * (N + 1)
to_search = [1]
while to_search:
    tmp = []
    for parent in to_search:
        for child in E[parent]:
            A[child] = parent
            E[child].remove(parent)
            tmp.append(child)
    to_search = tmp[:]
for i in range(2, N + 1):
    print(A[i])

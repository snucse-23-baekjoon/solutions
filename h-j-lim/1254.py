import sys


def area(p1, p2, p3):
    return (1/2) * abs(p1[0] * p2[1] + p2[0] * p3[1] + p3[0] * p1[1]
                       - p2[0] * p1[1] - p3[0] * p2[1] - p1[0] * p3[1])


N = int(input())
V = []
for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    V.append((a, b))
A = []
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            A.append(area(V[i], V[j], V[k]))
print(max(A))

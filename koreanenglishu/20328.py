from sys import stdin
stdin = open("../input.txt", 'r')

def q1():
    for i in range(l):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][3], G[i][2], G[i][1], G[i][0]

def q2():
    for i in range(l):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][1], G[i][0], G[i][3], G[i][2]

def q3():
    for i in range(l):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][3], G[i][0], G[i][1], G[i][2]

def q4():
    for i in range(l):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][1], G[i][2], G[i][3], G[i][0]

def q5():
    for i in range(l, N):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][3], G[i][2], G[i][1], G[i][0]

def q6():
    for i in range(l, N):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][1], G[i][0], G[i][3], G[i][2]

def q7():
    for i in range(l, N):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][3], G[i][0], G[i][1], G[i][2]

def q8():
    for i in range(l, N):
        G[i][0], G[i][1], G[i][2], G[i][3] = \
            G[i][1], G[i][2], G[i][3], G[i][0]


A = []
N, R = map(int, stdin.readline().split())
G = [[0, 1, 2, 3] for _ in range(N)]
F = {
    1: q1, 2: q2, 3: q3, 4: q4,
    5: q5, 6: q6, 7: q7, 8: q8
}

for _ in range(1 << N):
    A.append(list(map(int, stdin.readline().split())))
for _ in range(R):
    k, l = map(int, stdin.readline().split()); F[k]()
for n in range(N):
    S, s = 1 << N, 1 << n
    for R in range(0, S, s << 1):
        for C in range(0, S, s << 1):
            for r in range(s):
                for c in range(s):
                    T = A[R + r][C + c], A[R + r][C + c + s], \
                        A[R + r + s][C + c + s], A[R + r + s][C + c]
                    T = T[G[n][0]], T[G[n][1]], T[G[n][2]], T[G[n][3]]
                    A[R + r][C + c], A[R + r][C + c + s], \
                        A[R + r + s][C + c + s], A[R + r + s][C + c] = T

print('\n'.join(map(
    lambda x: ' '.join(map(str, x)), A
)))

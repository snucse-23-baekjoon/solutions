from sys import stdin
stdin = open("../input.txt", 'r')

def q1():
    global INV1, G1, G2, G3, G4
    G1, G2, G3, G4 = G4, G3, G2, G1
    INV1 ^= 1

def q2():
    global INV2, G1, G2, G3, G4
    G1, G2, G3, G4 = G2, G1, G4, G3
    INV2 ^= 1

def q3():
    global INV1, INV2, INV3, G1, G2, G3, G4
    G1, G2, G3, G4 = G4, G1, G2, G3
    INV1, INV2, INV3 = INV2, INV1 ^ 1, INV3 ^ 1

def q4():
    global INV1, INV2, INV3, G1, G2, G3, G4
    G1, G2, G3, G4 = G2, G3, G4, G1
    INV1, INV2, INV3 = INV2 ^ 1, INV1, INV3 ^ 1

def q5():
    global G1, G2, G3, G4
    G1, G2, G3, G4 = G4, G1, G2, G3

def q6():
    global G1, G2, G3, G4
    G1, G2, G3, G4 = G2, G3, G4, G1

N, M, R = map(int, stdin.readline().split())
n, m = N // 2, M // 2
G1 = [[0] * m for _ in range(n)]
G2 = [[0] * m for _ in range(n)]
G3 = [[0] * m for _ in range(n)]
G4 = [[0] * m for _ in range(n)]

for i in range(n):
    arr = map(int, stdin.readline().split())
    for j in range(m): G1[i][j] = next(arr)
    for j in range(m): G2[i][j] = next(arr)
for i in range(n):
    arr = map(int, stdin.readline().split())
    for j in range(m): G4[i][j] = next(arr)
    for j in range(m): G3[i][j] = next(arr)

INV1, INV2, INV3 = 0, 0, 0
funcs = [None, q1, q2, q3, q4, q5, q6]
for q in map(int, stdin.readline().split()): funcs[q]()

if INV3:
    n, m = m, n
    G1 = list(map(list, zip(*G1)))
    G2 = list(map(list, zip(*G2)))
    G3 = list(map(list, zip(*G3)))
    G4 = list(map(list, zip(*G4)))

if INV1:
    for G in [G1, G2, G3, G4]:
        for i in range(n // 2):
            for j in range(m):
                G[i][j], G[-1 - i][j] = G[-1 - i][j], G[i][j]

if INV2:
    for G in [G1, G2, G3, G4]:
        for i in range(n):
            for j in range(m // 2):
                G[i][j], G[i][-1 - j] = G[i][-1 - j], G[i][j]

for i in range(n):
    print(*G1[i], end=' ')
    print(*G2[i])
for i in range(n):
    print(*G4[i], end=' ')
    print(*G3[i])

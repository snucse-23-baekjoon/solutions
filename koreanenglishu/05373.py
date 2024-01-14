from sys import stdin
stdin = open("../input.txt", 'r')

def u_plus():
    for i in range(3):
        F[0][i], L[0][i], B[0][i], R[0][i] = \
            R[0][i], F[0][i], L[0][i], B[0][i]
    for i in range(2):
        U[0][i], U[i][2], U[2][2 - i], U[2 - i][0] = \
            U[2 - i][0], U[0][i], U[i][2], U[2][2 - i]

def u_minus():
    for i in range(3):
        F[0][i], L[0][i], B[0][i], R[0][i] = \
            L[0][i], B[0][i], R[0][i], F[0][i]
    for i in range(2):
        U[0][i], U[i][2], U[2][2 - i], U[2 - i][0] = \
            U[i][2], U[2][2 - i], U[2 - i][0], U[0][i]

def d_plus():
    for i in range(3):
        F[2][i], R[2][i], B[2][i], L[2][i] = \
            L[2][i], F[2][i], R[2][i], B[2][i]
    for i in range(2):
        D[i][0], D[2][i], D[2 - i][2], D[0][2 - i] = \
            D[0][2 - i], D[i][0], D[2][i], D[2 - i][2]

def d_minus():
    for i in range(3):
        F[2][i], R[2][i], B[2][i], L[2][i] = \
            R[2][i], B[2][i], L[2][i], F[2][i]
    for i in range(2):
        D[i][0], D[2][i], D[2 - i][2], D[0][2 - i] = \
            D[2][i], D[2 - i][2], D[0][2 - i], D[i][0]

def f_plus():
    for i in range(3):
        U[2][i], R[i][0], D[2][2 - i], L[2 - i][2] = \
            L[2 - i][2], U[2][i], R[i][0], D[2][2 - i]
    for i in range(2):
        F[0][i], F[i][2], F[2][2 - i], F[2 - i][0] = \
            F[2 - i][0], F[0][i], F[i][2], F[2][2 - i]

def f_minus():
    for i in range(3):
        U[2][i], R[i][0], D[2][2 - i], L[2 - i][2] = \
            R[i][0], D[2][2 - i], L[2 - i][2], U[2][i]
    for i in range(2):
        F[0][i], F[i][2], F[2][2 - i], F[2 - i][0] = \
            F[i][2], F[2][2 - i], F[2 - i][0], F[0][i]

def b_plus():
    for i in range(3):
        U[0][i], L[2 - i][0], D[0][2 - i], R[i][2] = \
            R[i][2], U[0][i], L[2 - i][0], D[0][2 - i]
    for i in range(2):
        B[0][i], B[i][2], B[2][2 - i], B[2 - i][0] = \
            B[2 - i][0], B[0][i], B[i][2], B[2][2 - i]

def b_minus():
    for i in range(3):
        U[0][i], L[2 - i][0], D[0][2 - i], R[i][2] = \
            L[2 - i][0], D[0][2 - i], R[i][2], U[0][i]
    for i in range(2):
        B[0][i], B[i][2], B[2][2 - i], B[2 - i][0] = \
            B[i][2], B[2][2 - i], B[2 - i][0], B[0][i]

def l_plus():
    for i in range(3):
        U[i][0], F[i][0], D[2 - i][0], B[2 - i][2] = \
            B[2 - i][2], U[i][0], F[i][0], D[2 - i][0]
    for i in range(2):
        L[0][i], L[i][2], L[2][2 - i], L[2 - i][0] = \
            L[2 - i][0], L[0][i], L[i][2], L[2][2 - i]

def l_minus():
    for i in range(3):
        U[i][0], F[i][0], D[2 - i][0], B[2 - i][2] = \
            F[i][0], D[2 - i][0], B[2 - i][2], U[i][0]
    for i in range(2):
        L[0][i], L[i][2], L[2][2 - i], L[2 - i][0] = \
            L[i][2], L[2][2 - i], L[2 - i][0], L[0][i]

def r_plus():
    for i in range(3):
        U[i][2], B[2 - i][0], D[2 - i][2], F[i][2] = \
            F[i][2], U[i][2], B[2 - i][0], D[2 - i][2]
    for i in range(2):
        R[0][i], R[i][2], R[2][2 - i], R[2 - i][0] = \
            R[2 - i][0], R[0][i], R[i][2], R[2][2 - i]

def r_minus():
    for i in range(3):
        U[i][2], B[2 - i][0], D[2 - i][2], F[i][2] = \
            B[2 - i][0], D[2 - i][2], F[i][2], U[i][2]
    for i in range(2):
        R[0][i], R[i][2], R[2][2 - i], R[2 - i][0] = \
            R[i][2], R[2][2 - i], R[2 - i][0], R[0][i]

funcs = {
    "U+": u_plus, "U-": u_minus,
    "D+": d_plus, "D-": d_minus,
    "F+": f_plus, "F-": f_minus,
    "B+": b_plus, "B-": b_minus,
    "L+": l_plus, "L-": l_minus,
    "R+": r_plus, "R-": r_minus,
}

for _ in range(int(stdin.readline())):
    U = [['w'] * 3 for _ in range(3)]
    D = [['y'] * 3 for _ in range(3)]
    F = [['r'] * 3 for _ in range(3)]
    B = [['o'] * 3 for _ in range(3)]
    L = [['g'] * 3 for _ in range(3)]
    R = [['b'] * 3 for _ in range(3)]
    _ = int(stdin.readline())
    for query in stdin.readline().split():
        funcs[query]()
        # print('\n'.join(map(lambda x: ''.join(x), U)))
        # print()
    print('\n'.join(map(lambda x: ''.join(x), U)))

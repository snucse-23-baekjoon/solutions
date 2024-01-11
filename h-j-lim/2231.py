def chessboard(mat):
    w = 0
    b = 0
    for r in range(8):
        for c in range(8):
            if mat[r][c] == 'W':
                if r % 2 + c % 2 == 1:
                    w += 1
                else:
                    b += 1
            else:
                if r % 2 + c % 2 == 1:
                    b += 1
                else:
                    w += 1
    if w < b:
        return w
    else:
        return b


def matrixslice(mat, n1, n2):
    matrix_sliced = []
    for r in range(n1, n1 + 8):
        matrix_sliced.append(mat[r][n2: n2 + 8])
    return matrix_sliced


N, M = map(int, input().split())
matrix = [input() for _ in range(N)]
matrix = list(map(list, matrix))
m = 65
for i in range(N - 7):
    for j in range(M - 7):
        tmp_mat = matrixslice(matrix, i, j)
        if chessboard(tmp_mat) < m:
            m = chessboard(tmp_mat)
print(m)

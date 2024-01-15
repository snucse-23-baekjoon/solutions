def matrix_mul(m1, m2):
    n = len(m)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if m1[i][k] * m2[k][j]:
                    result[i][j] = 1
                    break
    return result
    
def matrix_add(m1, m2):
    n = len(m1)
    result = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            result[i][j] = 1 if m1[i][j]+m2[i][j] else 0
    return result

from sys import stdin
n = int(stdin.readline())
m = [list(map(int, stdin.readline().split())) for i in range(n)]
lst = [m]
for i in range(n):
    lst.append(matrix_mul(m, lst[i]))
result = m
for i in range(n):
    result = matrix_add(result, lst[i+1])
for i in range(n):
    for j in range(n):
        print(result[i][j], end=' ')
    print()
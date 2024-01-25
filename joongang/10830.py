def mul(m1, m2, n):
    result = []
    for i in range(n):
        tmp = []
        for j in range(n):
            s = 0
            for k in range(n):
                s += m1[i][k] * m2[k][j]
            tmp.append(s%1000)
        result.append(tmp)
    return result

def power(A, b):
    if b == 1:
        return A
    if b == 2:
        return mul(A, A, n)
    Aprime = power(A, b//2)
    if b%2:
        return mul(mul(Aprime, Aprime, n), A, n)
    return mul(Aprime, Aprime, n)

from sys import stdin
n, b = map(int, stdin.readline().split())
A = [list(map(int, stdin.readline().split())) for i in range(n)]
result = power(A, b)
for i in range(n):
    for j in range(n):
        print(result[i][j]%1000, end=' ')
    print()
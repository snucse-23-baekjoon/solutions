def mul(m1, m2):
    result = []
    for i in range(8):
        tmp = []
        for j in range(8):
            s = 0
            for k in range(8):
                s += m1[i][k] * m2[k][j]
            tmp.append(s%div)
        result.append(tmp)
    return result

def power(A, b):
    if b == 1:
        return A
    if b == 2:
        return mul(A, A)
    Aprime = power(A, b//2)
    if b%2:
        return mul(mul(Aprime, Aprime), A)
    return mul(Aprime, Aprime)

div = 1000000007
n = int(input())
m = [[0, 1, 1, 0, 0, 0, 0, 0],
[1, 0, 1, 1, 0, 0, 0, 0],
[1, 1, 0, 1, 0, 1, 0, 0],
[0, 1, 1, 0, 1, 1, 0, 0],
[0, 0, 0, 1, 0, 1, 1, 0],
[0, 0, 1, 1, 1, 0, 0, 1],
[0, 0, 0, 0, 1, 0, 0, 1],
[0, 0, 0, 0, 0, 1, 1, 0]]
powered = power(m, n)
print(powered[0][0]%div)
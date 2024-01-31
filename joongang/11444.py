def mul(m1, m2):
    result = []
    for i in range(2):
        cur = []
        for j in range(2):
            s = 0
            for k in range(2):
                s += m1[i][k] * m2[k][j]
            cur.append(s%1000000007)
        result.append(cur)
    return result

def power(m, n):
    if n == 0:
        return [[1, 0], [0, 0]]
    if n == 1:
        return m
    if n == 2:
        return mul(m, m)
    tmp = power(m, n//2)
    if n % 2:
        return mul(mul(tmp, tmp), m)
    return mul(tmp, tmp)

from sys import stdin
n = int(stdin.readline())
m = [[1, 1], [1, 0]]
print(power(m, n-1)[0][0]%1000000007)
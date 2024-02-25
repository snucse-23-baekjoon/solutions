from sys import stdin
stdin = open("../input.txt", "r")

class Frac:
    def __init__(self, num, den):
        g = gcd(num, den)
        if den < 0: num, den = -num, -den
        self.num = num // g
        self.den = den // g
    
    def __str__(self):
        if self.den == 1: return f"{self.num}"
        else: return f"{self.num}/{self.den}"

def gcd(a, b):
    a, b = abs(a), abs(b)
    while b: a, b = b, a % b
    return a

def parse_coef(side):
    a = b = c = 0
    side = ["+"] + side.split()
    for i in range(len(side) // 2):
        sign, term = side[2 * i : 2 * i + 2]
        sign = -1 if sign == "-" else 1
        if term[-1] in "xy": coef = term[:-1]
        else: coef = term
        if coef == "" or coef == "-": coef += "1"
        if term[-1] == 'x': a += sign * int(coef)
        elif term[-1] == 'y': b += sign * int(coef)
        else: c += sign * int(coef)
    return a, b, c

T = int(stdin.readline())
for _ in range(T):
    sol_x = sol_y = "don't know"
    A, B = [[0, 0], [0, 0]], [0, 0]
    for i in range(2):
        lhs, rhs = stdin.readline().rstrip().split('=')
        a, b, c = parse_coef(lhs)
        d, e, f = parse_coef(rhs)
        A[i][0], A[i][1], B[i] = a - d, b - e, f - c
    a, b, c, d, e, f = *(A[0]), *(A[1]), *B
    if a * d - b * c:
        sol_x = Frac(d * e - b * f, a * d - b * c)
        sol_y = Frac(a * f - c * e, a * d - b * c)
    else:
        if a and c:
            g = gcd(a, c)
            c, d, f = 0, 0, e * (c // g) - f * (a // g)
        elif b and d:
            g = gcd(b, d)
            c, d, f = 0, 0, e * (d // g) - f * (b // g)
        elif c or d or (not a and not b and e):
            a, b, c, d, e, f = c, d, a, b, f, e
        if not f:
            if a and not b: sol_x = Frac(e, a)
            elif not a and b: sol_y = Frac(e, b)
    stdin.readline()
    print(sol_x, sol_y, sep='\n')
    if _ < T - 1: print()

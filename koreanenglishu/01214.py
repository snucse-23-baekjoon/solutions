import sys
sys.stdin = open("../input.txt", 'r')

D, P, Q = map(int, sys.stdin.readline().split())
P, Q = (Q, P) if P > Q else (P, Q)

r0, r1 = P, Q
s0, s1 = 1, 0
t0, t1 = 0, 1

while r1:
    q, r = divmod(r0, r1)
    r0, r1 = r1, r
    s0, s1 = s1, s0 - q * s1
    t0, t1 = t1, t0 - q * t1

GCD, M, N = r0, -s0, t0
R, S = Q // GCD, P // GCD
C = min(M // R, N // S)
M, N = M - R * C, N - S * C

MIN = max(D, P)
m = -(-MIN // P) - 1
c = -(-(MIN - P * m) // GCD)
m, n = m - M * c, N * c
while -(m // R) > (n // S):
    m, n = m - M, n + N
ANS = P * m + Q * n

print(ANS)

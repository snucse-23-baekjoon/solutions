import sys
sys.stdin = open("../input.txt", 'r')

is_prime = [True] * 1_000_001
for p in range(2, 1_001):
    if is_prime[p]:
        q = 2 * p
        while q < 1_000_001:
            is_prime[q] = False
            q += p

primes = []
for p in range(2, 1_000_001):
    if is_prime[p]:
        primes.append(p)

a, b = map(int, sys.stdin.readline().split())
is_no_square = [True] * (b - a + 1)
ans = b - a + 1

for p in primes:
    q = p * p
    if q > b:
        break

    r = -(-a // q) * q
    while r <= b:
        if is_no_square[r - a]:
            is_no_square[r - a] = False
            ans -= 1
        r += q

print(ans)

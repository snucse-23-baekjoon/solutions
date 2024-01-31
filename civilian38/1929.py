m, n = tuple(map(int, input().split()))
numbers = [False, False] + [True] * (n - 1)
primes = list()

for i in range(2, n + 1):
    if numbers[i]:
        primes.append(i)
    for j in range(2 * i, n + 1, i):
        numbers[j] = False
        
any(map(print, filter(lambda x: x >= m, primes)))
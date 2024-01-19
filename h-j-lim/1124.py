num_list = list(range(50000))
prime_list = []
for i in range(2, 50000):
    if num_list[i]:
        prime_list.append(num_list[i])
        num_list[i:: i] = [0] * ((len(num_list) - 1) // num_list[i])
prime_set = set(prime_list)
A, B = map(int, input().split())
count = 0
for num in range(A, B + 1):
    num_of_primes = 0
    for prime in prime_list:
        while num % prime == 0:
            num_of_primes += 1
            num = num // prime
        if num == 1:
            break
        if num in prime_set:
            num_of_primes += 1
            break
    if num_of_primes in prime_set:
        count += 1
print(count)

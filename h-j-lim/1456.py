def power(n, k):  # n^k
    if k == 0:
        return 1
    if k % 2 == 0:
        return power(n, k // 2) * power(n, k // 2)
    if k % 2 == 1:
        return power(n, k // 2) * power(n, k // 2) * n


A, B = map(int, input().split())
B_sqrt = int(B ** (1/2))
num_list = list(range(B_sqrt + 1))
list_prime = []
list_ans = []
for i in range(2, B_sqrt + 1):
    if num_list[i]:
        list_prime.append(num_list[i])
        num_list[i::i] = (B_sqrt // i) * [0]
for prime in list_prime:
    i = 2
    while power(prime, i) <= B:
        list_ans.append(power(prime, i))
        i += 1
print(len(list(filter(lambda x: x >= A, list_ans))))

N, K = map(int, input().split())
num_of_digits = 0
tmp = N
while tmp:
    tmp = tmp // 10
    num_of_digits += 1
set_of_remainders = set()
count = 1
found = True
if N % K == 0:
    print(1)
else:
    original_N = N
    while N % K:
        remainder = N % K
        if remainder in set_of_remainders:
            found = False
            break
        else:
            set_of_remainders.add(remainder)
        N = remainder * (10 ** num_of_digits) + original_N
        count += 1
    if found:
        print(count)
    else:
        print(-1)

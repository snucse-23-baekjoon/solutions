N, k = map(int, input().split())
tmp = N
num_of_digits = 0
while tmp:
    tmp = tmp // 10
    num_of_digits += 1
i = 1
len_of_num = 0
while i < num_of_digits:
    len_of_num += 9 * (10 ** (i - 1)) * i
    i += 1
len_of_num += (N - (10 ** (i - 1)) + 1) * i
if k > len_of_num:
    print(-1)
else:
    j = 1
    start = 0
    while start + 9 * (10 ** (j - 1)) * j < k:
        start += 9 * (10 ** (j - 1)) * j
        j += 1
    start += 1
    nth = (k - start) // j
    num = 10 ** (j - 1) + nth
    print(str(num)[k - (start + nth * j)])

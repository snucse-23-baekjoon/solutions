def check(n):
    i = 2
    count = 0
    while i * i <= n:
        if factor[i] == -1:
            pass
        elif factor[i] % 2:
            count += n // (i * i)
        else:
            count -= n // (i * i)
        i += 1
    return count

MAX = 200001
factor = [0] * MAX
for p in range(2, MAX):
    if factor[p] == 0:
        r = p
        while r < MAX:
            if factor[r] != -1:
                factor[r] += 1
            r += p
        r = q = p * p
        while r < MAX:
            factor[r] = -1
            r += q

K = int(input())
left, right = 1, 4 * K + 1
while right - left > 1:
    center = (left + right + 1) // 2
    if K <= check(center - 1):
        right = center
    else:
        left = center
print(left)

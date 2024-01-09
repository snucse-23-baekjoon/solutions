ans = ''
N, B = map(int, input().split())
while N:
    remain = N % B
    if 0 <= remain <= 9:
        remain = str(remain)
    else:
        remain = chr(ord('A') + remain - 10)
    ans = remain + ans
    N = N // B
print(ans)


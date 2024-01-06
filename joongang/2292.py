n = int(input()) - 1
ans = 1
while n > 0:
    n -= 6 * ans
    ans += 1
print(ans)
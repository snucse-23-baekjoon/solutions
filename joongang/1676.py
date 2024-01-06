n = int(input())
fact = 1
while n > 0:
    fact *= n
    n -= 1
cnt = 0
while fact % 10 == 0:
    cnt += 1
    fact //= 10
print(cnt)
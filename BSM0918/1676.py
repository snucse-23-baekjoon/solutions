N = int(input())
factorial_N = 1
for i in range(1, N+1):
    factorial_N *= i

factorial_N = str(factorial_N)

i = -1
cnt = 0
while factorial_N[i] == '0':
    cnt += 1
    i -= 1

print(cnt)
    
    

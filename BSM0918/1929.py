M, N = map(int, input().split())

prime = [1 for _ in range(N+1)]
prime[0] = prime[1] = 0  # 0과 1은 소수가 아님

# 에라토스테네스의 체 알고리즘 수행
for i in range(2, int(N**0.5) + 1):
    if prime[i]:
        for j in range(i*2, N+1, i):
            prime[j] = 0

# M 이상 N 이하의 소수 출력
for i in range(M, N+1):
    if prime[i]:
        print(i)

            
            

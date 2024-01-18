N, K = map(int, input().split())
B = []
while N:
    B.append(N % 2)
    N = N // 2
if B.count(1) <= K:
    print(0)
else:
    i = 0
    while B[:i].count(1) < B.count(1) - K + 1:
        i += 1
    Target = 2 ** i
    a = 0
    for j in range(i):
        a += B[j] * (2 ** j)
    print(Target - a)

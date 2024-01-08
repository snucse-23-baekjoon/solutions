A = []
M = 0
x = ''
for i in range(5):
    a = list(input())
    A.append(a)
    if M < len(a):
        M = len(a)
for i in range(M):
    for j in range(5):
        if i < len(A[j]):
            x = x + A[j][i]
print(x)

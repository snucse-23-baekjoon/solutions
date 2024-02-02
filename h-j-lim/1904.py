N = int(input())
if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    n1 = 1
    n2 = 2
    for i in range(N - 2):
        tmp = n2
        n2 = (n1 + n2) % 15746
        n1 = tmp
    print(n2)

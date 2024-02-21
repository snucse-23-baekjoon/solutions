N = int(input())
L = list(map(int, input().split()))
if N == 1:
    print('A')
elif N == 2:
    if L[0] == L[1]:
        print(L[0])
    else:
        print('A')
else:
    if L[0] == L[1]:
        flag = True
        for i in range(2, N):
            if L[i] != L[0]:
                flag = False
        if flag:
            print(L[0])
        else:
            print('B')
    else:
        a = (L[2] - L[1]) // (L[1] - L[0])
        b = L[1] - L[0] * a
        flag = True
        if not(a % 1 == 0 and b % 1 == 0):
            flag = False
        for i in range(2, N):
            if L[i] != a * L[i - 1] + b:
                flag = False
        if flag:
            print(a * L[N - 1] + b)
        else:
            print('B')

N = int(input())
D = {N: 0}
while 1 not in D.keys():
    tmp = D.copy()
    for num in tmp.keys():
        if num % 3 == 0 and (num // 3) not in D.keys():
            D[num // 3] = D[num] + 1
        if num % 2 == 0 and (num // 2) not in D.keys():
            D[num // 2] = D[num] + 1
        if (num - 1) not in D.keys():
            D[num - 1] = D[num] + 1
print(D[1])

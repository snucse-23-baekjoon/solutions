N = int(input())
L = []
nearest_sqrt = int(N ** 0.5)
for i in range(1, nearest_sqrt + 1):
    L.append(i ** 2)
found = False
if nearest_sqrt ** 2 == N:
    found = True
    print(1)
if not found:
    for i in range(nearest_sqrt):
        if N - L[i] in L:
            found = True
            print(2)
            break
if not found:
    for i in range(nearest_sqrt):
        for j in range(nearest_sqrt):
            if N - L[i] - L[j] in L:
                found = True
                print(3)
                break
        if found:
            break
if not found:
    found = True
    print(4)

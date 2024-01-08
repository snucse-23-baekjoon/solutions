X = int(input())
D = 0

while X > 0:
    if X%2 == 1:
        D += 1
        X = (X-1)/2
    else:
        X = X/2

print(D)
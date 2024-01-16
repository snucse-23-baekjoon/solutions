import math
n = int(input())
if int(math.sqrt(n)) == math.sqrt(n):
    print(1)
    exit(0)
for i in range(1, int(math.sqrt(n))+1):
    if int(math.sqrt(n-i**2)) == math.sqrt(n-i**2):
        print(2)
        exit(0)
for i in range(1, int(math.sqrt(n))+1):
    for j in range(1, int(math.sqrt(n-i**2))+1):
        if int(math.sqrt(n-i**2-j**2)) == math.sqrt(n-i**2-j**2):
            print(3)
            exit(0)
print(4)
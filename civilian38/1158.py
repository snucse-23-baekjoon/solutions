n, k = tuple(map(int, input().split()))
k -= 1

circle = [i for i in range(1, 1 + n)]
index = k
print("<", end="")
if len(circle) > 1:
    while circle:
        print(str(circle.pop(index)), end=", ")
        index = (index + k) % len(circle)
        if len(circle) == 1:
            print(str(circle.pop(0))+">")
else:
    if circle:
        print(str(circle.pop()) + ">")
    else:
        print("<>")
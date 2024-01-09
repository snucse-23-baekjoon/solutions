count = 1
a, b = 0, 0
n = int(input())
while a + count < n:
    a = a + count
    count += 1
b = n - a - 1
c = count - b
d = 1 + b
if count % 2:
    print(str(c) + '/' + str(d))
else:
    print(str(d) + '/' + str(c))

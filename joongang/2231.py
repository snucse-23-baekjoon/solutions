n = int(input())
l = len(str(n))
m = max(1, n - 9*l)
M = max(1, n - l)
for i in range(m, M+2):
    s = i
    for j in range(len(str(i))):
        s += int(str(i)[j])
    if s == n:
        break
print(i if i<M+1 else 0)
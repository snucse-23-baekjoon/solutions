l = int(input())
s = input()
r = 31
m = 1234567891
h = 0
for i in range(l):
    h += (ord(s[i]) - ord('a') + 1) * (r**i)
h %= m
print(h)
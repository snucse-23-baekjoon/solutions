s = input().upper()
M = 0
a = ""
for i in set(s):
    c = s.count(i)
    if c == M:
        a = "?"
    if c > M:
        a = i
        M = c
print(a)
Str = input()
S = set()
for i in range(len(Str)):
    for j in range(len(Str) - i):
        S.add(Str[i: i + j + 1])
print(len(S))

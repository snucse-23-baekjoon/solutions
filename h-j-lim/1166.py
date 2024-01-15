S = input()
D = {}
for i in range(len(S)):
    if S[i] not in D:
        D[S[i]] = 1
    else:
        D[S[i]] += 1
L_count = list(map(lambda x: x % 2, D.values()))
lexico = sorted(list(D.keys()))
if (len(S) % 2 == 0 and any(L_count)) or (len(S) % 2 == 1 and L_count.count(1) != 1):
    print("I'm Sorry Hansoo")
else:
    half, mid = '', ''
    for alph in lexico:
        half += alph * (D[alph] // 2)
        if D[alph] % 2 == 1:
            mid = alph
    print(half + mid + ''.join(reversed(list(half))))

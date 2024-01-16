S = input().rstrip()
p = (len(S) + 1) // 2
excess = 0
while p < len(S):
    if list(S[2 * p - len(S) - 1:p - 1]) == list(reversed(S[p:])):
        excess = 2 * p - len(S) - 1
        break
    if list(S[2 * p - len(S):p]) == list(reversed(S[p:])):
        excess = 2 * p - len(S)
        break
    p += 1
if p == len(S):
    print(2 * len(S) - 1)
else:
    print(len(S) + excess)

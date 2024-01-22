from sys import stdin
stdin = open("../input.txt", 'r')

def kmp(t):
    j, c = 0, 0
    for i in range(len(t)):
        while j > 0 and t[i] != p[j]: j = pi[j - 1]
        if t[i] == p[j]:
            if j == len(p) - 1: j = pi[j]; c += 1
            else: j += 1
    return c

c = 1
while True:
    try: n = int(stdin.readline())
    except: break
    p = stdin.readline().rstrip()

    # GENERATE PI ARRAY OF PATTERN
    pi = [0] * len(p); j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]: j = pi[j - 1]
        if p[i] == p[j]: j += 1; pi[i] = j

    # INITIALIZE DP ARRAY, PREFIXES, AND SUFFIXES
    dp = [0] * (n + 1)
    if p == '0': dp[0] = 1
    elif n and p == '1': dp[1] = 1
    if len(p) > 1: pref1, suff1, pref2, suff2 = '0011'
    else: pref1, suff1, pref2, suff2 = '', '', '', ''

    # DYNAMIC PROGRAMMING
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + kmp(suff2 + pref1)
        temp = pref2, suff2
        if len(pref2) < len(p) - 1:
            pref2 = pref2 + pref1[:len(p) - len(pref2) - 1]
        if len(suff1) < len(p) - 1:
            suff2 = suff2[len(suff1) - len(p) + 1:] + suff1
        else: suff2 = suff1
        pref1, suff1 = temp

    print(f'Case {c}:', dp[-1]); c += 1

import sys


T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    if N > 32:
        tmp = sys.stdin.readline()
        print(0)
    elif N > 16:
        L = sys.stdin.readline().rstrip().split()
        dict_mbti = {}
        for i in range(N):
            if L[i] not in dict_mbti.keys():
                dict_mbti[L[i]] = 1
            else:
                dict_mbti[L[i]] += 1
        if max(dict_mbti.values()) > 2:
            print(0)
        else:
            print(2)
    else:
        L = sys.stdin.readline().rstrip().split()
        res = 100
        for i in range(N - 2):
            for j in range(i + 1, N - 1):
                for k in range(j + 1, N):
                    tmp = 0
                    for a in range(4):
                        if L[i][a] != L[j][a]:
                            tmp += 1
                        if L[j][a] != L[k][a]:
                            tmp += 1
                        if L[k][a] != L[i][a]:
                            tmp += 1
                    if tmp < res:
                        res = tmp
        print(res)

from sys import stdin
n, m = map(int, stdin.readline().split())
d1 = dict()
for i in range(1, n+1):
    d1[i] = stdin.readline().rstrip()
d2 = dict()
for i in d1:
    d2[d1[i]] = i
for i in range(m):
    q = stdin.readline().rstrip()
    try:
        q = int(q)    
    except:
        pass
    if type(q) == type(1):
        print(d1[q])
    else:
        print(d2[q])
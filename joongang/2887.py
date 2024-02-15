def find(x):
    if x == uf[x]:
        return x
    uf[x] = find(uf[x])
    return uf[x]

def union(x, y):
    x = find(x)
    y = find(y)
    uf[y] = x

from sys import stdin
n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for i in range(n)]
xlst = []
ylst = []
zlst = []
for i in range(n):
    xlst.append([lst[i][0], i])
    ylst.append([lst[i][1], i])
    zlst.append([lst[i][2], i])
xlst.sort()
ylst.sort()
zlst.sort()
E = []
for cur in xlst, ylst, zlst:
    for i in range(n-1):
        E.append([cur[i][1], cur[i+1][1], abs(cur[i][0]-cur[i+1][0])])
E.sort(key = lambda x: x[2])
uf = [i for i in range(n)]
mst = []
cnt = 0
i = 0
while cnt < n-1:
    x, y, z = E[i]
    if find(x) != find(y):
        mst.append([x, y, z])
        union(x, y)
        cnt += 1
    i += 1
s = 0
for x, y, z in mst:
    s += z
print(s)
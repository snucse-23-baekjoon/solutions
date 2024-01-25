from sys import stdin
n = int(stdin.readline())
cur = list(map(int, stdin.readline().split()))
Mlst = cur.copy()
mlst = cur.copy()
for i in range(1, n):
    cur = list(map(int, stdin.readline().split()))
    Mlst = [cur[0] + max(Mlst[:2]), cur[1] + max(Mlst), cur[2] + max(Mlst[1:])]
    mlst = [cur[0] + min(mlst[:2]), cur[1] + min(mlst), cur[2] + min(mlst[1:])]
print(max(Mlst), min(mlst))
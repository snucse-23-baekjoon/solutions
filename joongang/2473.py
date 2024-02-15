from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
lst.sort()
lp = 0
mlp = 0
mmp = 1
mrp = n-1
ans = 10**10
while lp < n-2:
    mp = lp+1
    rp = n-1
    while mp < rp:
        s = lst[lp] + lst[mp] + lst[rp]
        if ans > abs(s):
            ans = abs(s)
            mlp = lp
            mmp = mp
            mrp = rp
        if s == 0:
            print(lst[mlp], lst[mmp], lst[mrp])
            exit(0)
        elif s < 0:
            mp += 1
        else:
            rp -= 1
    lp += 1
print(lst[mlp], lst[mmp], lst[mrp])
from sys import stdin
n = int(stdin.readline())
lst = list(map(int, stdin.readline().split()))
ans = 10**10
lp = 0
rp = n-1
mlp = 0
mrp = n-1
while lp < rp:
    tmp = lst[lp] + lst[rp]
    if abs(tmp) < ans:
        ans = abs(tmp)
        mlp = lp
        mrp = rp
    if tmp < 0:
        lp += 1
    elif tmp > 0:
        rp -= 1
    else:
        break
print(lst[mlp], lst[mrp])
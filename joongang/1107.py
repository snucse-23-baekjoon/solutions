n = int(input())
m = int(input())
breakdowns = []
if m:
    breakdowns = list(map(int, input().split()))
ans = abs(n-100)
for i in range(2*n+100):
    l = list(str(i))
    chk = 0
    for j in l:
        if int(j) in breakdowns:
            chk = 1
            break
    if chk:
        continue
    if ans > len(l) + abs(i-n):
        ans = len(l) + abs(i-n)
print(ans)
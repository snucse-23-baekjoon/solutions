a, b, v = map(int, input().split())
v -= a
ans = v // (a-b) + 1
if v % (a-b):
    ans += 1
print(ans)
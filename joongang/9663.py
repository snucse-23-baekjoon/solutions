def dfs(a):
    global ans
    if a == n:
        ans += 1
        return
    for i in range(n):
        if chk(a, i):
            queens[a] = i
            dfs(a+1)
     
def chk(a, b):
    for i in range(a):
        if queens[i]==b or i+queens[i]==a+b or i-queens[i]==a-b:
            return 0
    return 1
                

n = int(input())
queens = [0]*n
ans = 0
dfs(0)
print(ans)
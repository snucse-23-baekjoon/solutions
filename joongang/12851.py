def bfs(n, k):
    if n == k:
        return 0, 1
    visited = {i: 0 for i in range(100001)}
    visited[n] = 1
    q = deque([n])
    ans = 0
    while q:
        cur = q.popleft()
        tmp = visited[cur]
        if cur == k:
            t = tmp
            ans += 1
            continue
        for i in [cur-1, cur+1, cur*2]:
            if 0<=i<=100000 and (not visited[i] or visited[i] == visited[cur] + 1):
                visited[i] = visited[cur] + 1
                q.append(i)
    return t-1, ans
    
from collections import deque
n, k = map(int, input().split())
t, l = bfs(n, k)
print(t)
print(l)
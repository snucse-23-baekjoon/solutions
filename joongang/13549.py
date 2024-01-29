def dfs(n, k):
    visited = [0 for i in range(100001)]
    visited[n] = 1
    q = deque([n])
    ans = float('inf')
    while q:
        cur = q.popleft()
        if cur == k:
            ans = min(ans, visited[cur]-1)
            continue
        if 0<cur<=50000 and (not visited[cur*2] or visited[cur*2] > visited[cur]):
            visited[cur*2] = visited[cur]
            q.append(cur*2)
        for i in [cur-1, cur+1]:
            if 0<=i<=100000 and (not visited[i] or visited[i] > visited[cur]+1):
                visited[i] = visited[cur] + 1
                q.append(i)
    return ans
            
from sys import stdin
from collections import deque
n, k = map(int, stdin.readline().split())
print(dfs(n, k))
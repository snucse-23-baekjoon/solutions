def bfs(a, b):
    visited = {a: 1}
    q = deque([a])
    while q:
        cur = q.popleft()
        if cur == b:
            return visited[cur]
        if cur<=(5*10**8):
            q.append(cur*2)
            visited[cur*2] = visited[cur]+1
        if cur<10**8:
            q.append(cur*10+1)
            visited[cur*10+1] = visited[cur]+1
    return -1
    
from collections import deque
a, b = map(int, input().split())
print(bfs(a, b))
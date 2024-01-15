def bfs(a, b):
    visited = {a: ''}
    queue = deque([])
    queue.append(a)
    while queue:
        n = queue[0]
        D = (n*2) % 10000 
        S = n-1 if n else 9999
        d1, d2, d3, d4 = n//1000, (n%1000)//100, (n%100)//10, n%10
        L = d2*1000 + d3*100 + d4*10 + d1
        R = d4*1000 + d1*100 + d2*10 + d3
        if D not in visited:
            visited[D] = visited[n] + 'D'
            queue.append(D)
        if S not in visited:
            visited[S] = visited[n] + 'S'
            queue.append(S)
        if L not in visited:
            visited[L] = visited[n] + 'L'
            queue.append(L)
        if R not in visited:
            visited[R] = visited[n] + 'R'
            queue.append(R)
        if b in [D, S, L, R]:
            return visited[b]
        queue.popleft()
        
from sys import stdin
from collections import deque
t = int(stdin.readline())
for _ in range(t):
    a, b = map(int, stdin.readline().split())
    print(bfs(a, b))
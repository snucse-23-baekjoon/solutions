from sys import stdin
def bfs(lst, n, m):
    visited = [[0 for i in range(m)] for j in range(n)]
    visited[0][0] = 1
    queue = [(0, 0)]
    dist = 1
    level = (0, 0)
    while queue[0] != (n-1, m-1):
        if queue[0][1] < m-1 and lst[queue[0][0]][queue[0][1]+1] and not visited[queue[0][0]][queue[0][1]+1]:
            queue.append((queue[0][0], queue[0][1]+1))
            visited[queue[0][0]][queue[0][1]+1] = 1
        if queue[0][1] and lst[queue[0][0]][queue[0][1]-1] and not visited[queue[0][0]][queue[0][1]-1]:
            queue.append((queue[0][0], queue[0][1]-1))
            visited[queue[0][0]][queue[0][1]-1] = 1
        if queue[0][0] < n-1 and lst[queue[0][0]+1][queue[0][1]] and not visited[queue[0][0]+1][queue[0][1]]:
            queue.append((queue[0][0]+1, queue[0][1]))
            visited[queue[0][0]+1][queue[0][1]] = 1
        if queue[0][0] and lst[queue[0][0]-1][queue[0][1]] and not visited[queue[0][0]-1][queue[0][1]]:
            queue.append((queue[0][0]-1, queue[0][1]))
            visited[queue[0][0]-1][queue[0][1]] = 1
        if queue[0] == level:
            dist += 1
            level = queue[-1]
        queue.pop(0)
    print(dist)
        
n, m = map(int, stdin.readline().split())
lst = []
for i in range(n):
    lst.append(list(map(int, list(stdin.readline().rstrip()))))
bfs(lst, n, m)
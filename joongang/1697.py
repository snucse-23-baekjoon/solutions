def bfs(n, k):
    visited = {n}
    dist = 0
    level = n
    queue = [n]
    while queue and queue[0] != k:
        c = queue[0]
        if c-1 not in visited and c > 0:
            queue.append(c-1)
            visited.add(c-1)
        if c+1 not in visited and c < 100000:
            queue.append(c+1)
            visited.add(c+1)
        if 2*c not in visited and c < 66668:
            queue.append(2*c)
            visited.add(2*c)
        if level == c:
            dist += 1
            level = queue[-1]
        queue.pop(0)
    print(dist)
            
n, k = map(int, input().split())
bfs(n, k)
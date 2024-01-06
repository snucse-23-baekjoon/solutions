import sys
import heapq
sys.stdin = open("../input.txt", 'r')

T = int(sys.stdin.readline())
for _ in range(T):

    N, K = map(int, sys.stdin.readline().split())
    duration = list(map(int, sys.stdin.readline().split()))
    adj_list = [[] for _ in range(N)]
    in_deg = [0 for _ in range(N)]

    for __ in range(K):
        X, Y = map(int, sys.stdin.readline().split())
        u, v = X - 1, Y - 1
        adj_list[u].append(v)
        in_deg[v] += 1

    W = int(sys.stdin.readline())
    w = W - 1

    queue = []
    for u in range(N):
        if in_deg[u] == 0:
            heapq.heappush(queue, (duration[u], u))

    req_time, u = 0, -1
    while u != w:
        req_time, u = heapq.heappop(queue)
        for v in adj_list[u]:
            in_deg[v] -= 1
            if in_deg[v] == 0:
                heapq.heappush(queue, (req_time + duration[v], v))

    print(req_time)

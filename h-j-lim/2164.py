from collections import deque


N = int(input())
q = deque(list(range(1, N + 1)))
for i in range(N - 1):
    q.popleft()
    q.append(q[0])
    q.popleft()
print(q[0])

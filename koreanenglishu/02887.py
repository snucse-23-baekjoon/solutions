import sys
sys.stdin = open("../input.txt", 'r')

def find(parents, x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents, parents[x])
        return parents[x]

def union(parents, x, y):
    x = find(parents, x)
    y = find(parents, y)
    if x < y:
        parents[x] = y
    else:
        parents[y] = x

planets = []
N = int(sys.stdin.readline())
for i in range(N):
    x, y, z = map(int, sys.stdin.readline().split())
    planets.append((i, x, y, z))

planets_x = sorted(planets, key=lambda x: x[1])
planets_y = sorted(planets, key=lambda x: x[2])
planets_z = sorted(planets, key=lambda x: x[3])

edges = []

for i in range(N - 1):
    u, v = planets_x[i][0], planets_x[i + 1][0]
    w = abs(planets_x[i + 1][1] - planets_x[i][1])
    edges.append((u, v, w))

    u, v = planets_y[i][0], planets_y[i + 1][0]
    w = abs(planets_y[i + 1][2] - planets_y[i][2])
    edges.append((u, v, w))

    u, v = planets_z[i][0], planets_z[i + 1][0]
    w = abs(planets_z[i + 1][3] - planets_z[i][3])
    edges.append((u, v, w))

edges.sort(key=lambda x: x[2], reverse=True)

num_edges = 0
sum_weights = 0
parents = [i for i in range(N)]

while num_edges < N - 1:
    u, v, w = edges.pop()
    find(parents, u)
    find(parents, v)
    if parents[u] != parents[v]:
        union(parents, u, v)
        num_edges += 1
        sum_weights += w

print(sum_weights)

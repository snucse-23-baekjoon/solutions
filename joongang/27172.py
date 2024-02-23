from sys import stdin
n = int(stdin.readline())
card = list(map(int, stdin.readline().split()))
point = {i: 0 for i in card}
for i in card:
    cnt = 2
    while i*cnt <= 1000000:
        if i*cnt in point:
            point[i] += 1
            point[i*cnt] -= 1
        cnt += 1
for i in card:
    print(point[i], end=' ')
import sys


N, M, B = map(int, sys.stdin.readline().split())
land = []
num_blocks = 0
height_list = [0] * 257
for i in range(N):
    land += list(map(int, sys.stdin.readline().split()))
max_height, min_height = max(land), min(land)
for height in land:
    height_list[height] += 1
num_blocks = sum(map(lambda x: x * height_list[x], range(257)))
possible_height = (num_blocks + B) // (N * M)
lower_limit = min_height
if possible_height < max_height:
    upper_limit = possible_height
else:
    upper_limit = max_height
min_time = 512 * M * N + 1
ans_height = 0
for height in range(upper_limit, lower_limit - 1, -1):
    tmp = 0
    tmp += sum(map(lambda x: (height - x) * height_list[x], range(min_height, height)))
    tmp += sum(map(lambda x: 2 * (x - height) * height_list[x], range(height + 1, max_height + 1)))
    if tmp >= min_time:
        break
    else:
        min_time = tmp
        ans_height = height
print(min_time, ans_height)

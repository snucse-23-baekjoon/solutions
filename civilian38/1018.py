import sys

def counter(maps):
    board1 = ['WB' * 4, 'BW' * 4] * 4
    board2 = ['BW' * 4, 'WB' * 4] * 4
    count1, count2 = 0, 0
    for k in range(8):
        for l in range(8):
            if maps[k][l] != board1[k][l]:
                count1 += 1
            if maps[k][l] != board2[k][l]:
                count2 += 1
    return min((count1, count2))

height, length = tuple(map(int, sys.stdin.readline().split()))
board = [sys.stdin.readline().rstrip() for _ in range(height)]

answer = 64
for i in range(height - 7):
    for j in range(length - 7):
        answer = min((answer, counter([array[j: j + 8] for array in board[i: i + 8]])))

print(answer)
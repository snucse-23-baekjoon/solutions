import sys


def check_function(m, r, c, s):
    color = m[r][c]
    for i in range(r, r + s):
        for j in range(c, c + s):
            if m[i][j] != color:
                return False
    if color == 0:
        return 'white'
    else:
        return 'blue'


N = int(sys.stdin.readline())
full_paper = []
num_blue, num_white = 0, 0
for _ in range(N):
    full_paper.append(list(map(int, sys.stdin.readline().split())))
step_tmp = N
section_to_check = [[0, 0]]
while step_tmp:
    section_tmp = []
    for k in range(len(section_to_check)):
        row, col = section_to_check[k]
        ans_tmp = check_function(full_paper, row, col, step_tmp)
        if ans_tmp == 'white':
            num_white += 1
        elif ans_tmp == 'blue':
            num_blue += 1
        else:
            section_tmp.extend([[row, col], [row + step_tmp // 2, col], [row, col + step_tmp // 2], [row + step_tmp // 2, col + step_tmp // 2]])
    section_to_check = section_tmp[:]
    step_tmp = step_tmp // 2
print(num_white)
print(num_blue)

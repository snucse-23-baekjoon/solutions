from sys import stdin
stdin = open("../input.txt", 'r')

R, C = map(int, stdin.readline().split())
min_val, min_r, min_c = 1000, 0, 0
for r in range(R):
    for c, val in enumerate(map(int, stdin.readline().split())):
        if min_val > val and (r + c) & 1:
            min_val, min_r, min_c = val, r, c

if R & 1:
    temp = ''.join(('R' * (C - 1), 'D', 'L' * (C - 1), 'D'))
    for _ in range(R // 2): print(temp, end='')
    print('R' * (C - 1), end='')
elif C & 1:
    temp = ''.join(('D' * (R - 1), 'R', 'U' * (R - 1), 'R'))
    for _ in range(C // 2): print(temp, end='')
    print('D' * (R - 1), end='')
else:
    temp = ''.join(('R' * (C - 1), 'D', 'L' * (C - 1), 'D'))
    for _ in range(min_r // 2): print(temp, end='')
    for _ in range(min_c // 2): print('DRUR', end='')
    print('RD' if min_r & 1 else 'DR', end='')
    for _ in range((C - min_c - 1) // 2): print('RURD', end='')
    temp = ''.join(('D', 'L' * (C - 1), 'D', 'R' * (C - 1)))
    for _ in range((R - min_r - 1) // 2): print(temp, end='')
print()

# if R & 1: print(('R'*(C-1)+'D'+'L'*(C-1)+'D')*(R//2)+'R'*(C-1))
# elif C & 1: print(('D'*(R-1)+'R'+'U'*(R-1)+'R')*(C//2)+'D'*(R-1))
# else: print(
#     ('R'*(C-1)+'D'+'L'*(C-1)+'D')*(min_r//2)+'DRUR'*(min_c//2)
#     +('RD' if min_r & 1 else 'DR')+'RURD'*((C-min_c-1)//2)
#     +('D'+'L'*(C-1)+'D'+'R'*(C-1))*((R-min_r-1)//2)
# )

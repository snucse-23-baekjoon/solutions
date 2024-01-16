import sys

repeat = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))
reset = [-1] * repeat
backup = list(B)

for i in range(repeat):
    reset[B.index(max(B))] = min(A)
    B[B.index(max(B))] = -1
    A[A.index(min(A))] = max(A) + 1
    
answer = 0
for i in range(repeat):
    answer += reset[i] * backup[i]

print(answer)
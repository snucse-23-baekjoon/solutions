class vector:
    def __init__(self, a, b):
        self.x = a
        self.y = b
    def __add__(self, other):
        return vector(self.x+other.x, self.y+other.y)

def f(paper, n):
    first = paper[0][0]
    first = 0 if first else 1
    chk = 1
    for i in range(n):
        if first in paper[i]:
            chk = 0
            break
    if chk:
        return vector(1, 0) if first else vector(0, 1)
    else:
        paper1 = []
        paper2 = []
        paper3 = []
        paper4 = []
        for i in range(n//2):
            paper1.append(paper[i][:n//2])
            paper2.append(paper[i][n//2:])
            paper3.append(paper[i+n//2][:n//2])
            paper4.append(paper[i+n//2][n//2:])
        return f(paper1, n//2) + f(paper2, n//2) + f(paper3, n//2) + f(paper4, n//2)
        
from sys import stdin
n = int(stdin.readline())
paper = []
for i in range(n):
    paper.append(list(map(int, stdin.readline().split())))
ans = f(paper, n)
print(ans.x)
print(ans.y)
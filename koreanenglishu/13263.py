from sys import stdin
stdin = open("../input.txt", 'r')


class Frac:
    def __init__(self, num, den):
        self.num = num * (abs(den) // den)
        self.den = abs(den)

    def __lt__(self, other):
        return self.num * other.den \
            < self.den * other.num


class Line:  # f(x) = a * x + b
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def y(self, x):
        return self.a * x + self.b

    def intersect(self, other):
        return Frac(
            self.b - other.b,
            other.a - self.a
        )


class Stack:
    def __init__(self, line):
        self.stack_line = [line]
        self.stack_x = []

    def y(self, x):
        x_frac = Frac(x, 1)
        if not self.stack_x or \
                x_frac < self.stack_x[0]:
            right = 0
        else:
            left, right = 0, len(self.stack_x)
            while right - left > 1:
                center = (left + right + 1) // 2
                if x_frac < self.stack_x[center]:
                    right = center
                else:
                    left = center
        line = self.stack_line[right]
        self.stack_line = self.stack_line[right:]
        self.stack_x = self.stack_x[right:]
        return line.y(x)

    def push(self, line):
        while self.stack_x:
            l = self.stack_line[-1]
            x = self.stack_x[-1]
            if x < line.intersect(l):
                break
            self.stack_line.pop()
            self.stack_x.pop()
        l = self.stack_line[-1]
        self.stack_line.append(line)
        self.stack_x.append(line.intersect(l))


n = int(stdin.readline())
A = list(map(int, stdin.readline().split()))
B = list(map(int, stdin.readline().split()))
dp = [0] * n

stack = Stack(Line(B[0], 0))
for i in range(1, n - 1):
    dp[i] = stack.y(A[i])
    stack.push(Line(B[i], dp[i]))
print(stack.y(A[n - 1]))

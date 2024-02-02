from sys import stdin
stdin = open("../input.txt", 'r')


class Frac:
    def __init__(self, num, den):
        sign = -1 if den < 0 else 1
        self.num = num * sign
        self.den = den * sign

    def __lt__(self, other):
        return self.num * other.den \
            < self.den * other.num

    def __add__(self, other):
        return Frac(
            self.num + other * self.den,
            self.den
        )

    # def __sub__(self, other):
    #     return Frac(
    #         self.num * other.den - self.den * other.num,
    #         self.den * other.den
    #     )

    def __mul__(self, other):
        return Frac(
            self.num * other,
            self.den
        )

    # def __truediv__(self, other):
    #     return Frac(
    #         self.num * other.den,
    #         self.den * other.num
    #     )


class Line:  # f(x) = a * x + b
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def y(self, x):
        return x * self.a + self.b

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
        if not self.stack_x or \
                x < self.stack_x[0]:
            right = 0
        else:
            left, right = 0, len(self.stack_x)
            while right - left > 1:
                center = (left + right + 1) // 2
                if x < self.stack_x[center]:
                    right = center
                else:
                    left = center
        line = self.stack_line[right]
        # self.stack_line = self.stack_line[right:]
        # self.stack_x = self.stack_x[right:]
        return line.y(x)

    def push(self, line):
        while self.stack_x:
            l = self.stack_line[-2]
            x = self.stack_x[-1]
            if x < line.intersect(l):
                break
            self.stack_line.pop()
            self.stack_x.pop()

        l = self.stack_line[-1]
        if not self.stack_x and line.a == l.a:
            self.stack_line.pop()
            self.stack_line.append(line)
        else:
            self.stack_line.append(line)
            self.stack_x.append(line.intersect(l))


n = int(stdin.readline())
arr = []
for _ in range(n):
    x, y = map(int, stdin.readline().split())
    arr.append(Frac(y, x))

arr.sort(key=lambda f: (f.num, f.den))
dp = [0] * n
stack = Stack(Line(arr[0].num, arr[0].den))

for i in range(1, n):
    temp = stack.y(arr[i]) * arr[i].den
    dp[i] = max(dp[i - 1], temp.num // temp.den)
    # for line in stack.stack_line:
    #     print(f"{line.a}x+{line.b}", end=' ')
    # print()
    stack.push(Line(arr[i].num, arr[i].den))

print(dp[-1])

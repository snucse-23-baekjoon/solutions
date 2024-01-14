from sys import stdin
stdin = open("../input.txt", 'r')

class StrInt:
    def __init__(self, string):
        self.str = string

    def __lt__(self, other):
        gcd, temp = len(self.str), len(other.str)
        while temp:
            gcd, temp = temp, gcd % temp
        lcm = (len(self.str) * len(other.str)) // gcd
        p1, p2 = 0, 0
        for _ in range(lcm):
            if self.str[p1] != other.str[p2]:
                break
            p1 = (p1 + 1) % len(self.str)
            p2 = (p2 + 1) % len(other.str)
        return self.str[p1] < other.str[p2]

    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

N = int(stdin.readline())
arr = list(map(
    lambda x: StrInt(x), stdin.readline().split()
))
arr.sort()

ans = ''
while arr:
    strint = arr.pop()
    if ans or strint.str != '0':
        ans += strint.str
print(ans if ans else '0')

a, b = map(int, input().split())
c = int(input())
b += c
a += b//60
b %= 60
a %= 24
print(a, b)
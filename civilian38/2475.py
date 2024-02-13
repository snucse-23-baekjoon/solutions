a, b, c, d, e = map(int, input().split())
print(sum(map(lambda x: x * x, [a, b, c, d, e])) % 10)
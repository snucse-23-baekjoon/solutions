def cantor(x):
    y = len(x)
    if y == 1:
        return x
    return cantor(x[:y // 3]) + ' ' * (y // 3) + cantor(x[2 * (y // 3):])


while True:
    try:
        N = int(input())
        X = '-' * 3 ** N
        print(cantor(X))
    except EOFError:
        break

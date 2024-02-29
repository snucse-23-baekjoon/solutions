def a_to_b(a, b, x):
    if a == b:
        return x
    if a > b:
        return -1
    last_digit = b % 10
    if last_digit == 1:
        return a_to_b(a, b // 10, x + 1)
    elif last_digit % 2 == 0:
        return a_to_b(a, b // 2, x + 1)
    else:
        return -1


A, B = map(int, input().split())
print(a_to_b(A, B, 1))

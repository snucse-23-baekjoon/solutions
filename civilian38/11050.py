def factorial(number):
    if number:
        return number * factorial(number - 1)
    return 1

n, k = map(int, input().split())
print(factorial(n) // (factorial(k) * factorial(n - k)))